#!/usr/bin/env python3
"""Cloudflare Worker module to deploy Root certificate."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union

from CloudflareAPI import Cloudflare
from CloudflareAPI.exceptions import CFError

WORKER_NS_NAME_KEY = "CA_CERT_STORE"
WORKER_TITLE_KEY = "CA_TITLE"
WORKER_FINGERPRINT_KEY = "ROOT_CA_FINGERPRINT"
WORKER_CA_URL_KEY = "ROOT_CA_URL"


@dataclass
class WorkerData:
    """Data class which store basic information about the Root Certificate.

    Args:
        title (str): Title of the Worker
        fingerprint (str): Fingerprint to attach to the worker
        url (str): CA URL to attach to the worker
    """

    title: str
    fingerprint: str
    url: str

    def get_metadata(self, worker):
        """Generate and return metadata for the Cloudflare worker.

        Args:
            worker (CloudflareAPI.Worker): Worker instance of Cloudflare API.

        Returns:
            CloudflareAPI.Worker.Metadata: Contains metadata of the worker to
            be uploaded.
        """
        metadata = worker.Metadata()
        metadata.add_variable(WORKER_TITLE_KEY, self.title)
        metadata.add_variable(WORKER_FINGERPRINT_KEY, self.fingerprint)
        metadata.add_variable(WORKER_CA_URL_KEY, self.url)
        return metadata


class Worker(Cloudflare):
    """Cloudflare Worker class which handle the deployment of Root certificate."""

    def __init__(self, web_title: str, fingerprint: str, ca_url: str) -> None:
        """Initialise the Worker class.

        Args:
            web_title (str): Title of the Worker
            fingerprint (str): Fingerprint to attach to the worker
            ca_url (str): CA URL to attach to the worker
        """
        super().__init__()
        data = WorkerData(web_title, fingerprint, ca_url)
        self.metadata = data.get_metadata(self.worker)

    def loadCA(self, rootCA: str):
        """Load the CA certificate and write to the Cloudflare KV Namespace.

        Args:
            rootCA (str): Root Certificate file location
        """
        rootca: Optional[Union[bytes, str]] = None
        try:
            namespace = self.store.get_ns(WORKER_NS_NAME_KEY)
        except CFError:
            namespace = self.store.create(WORKER_NS_NAME_KEY)
        try:
            rootca = Path(rootCA).read_text()
            namespace.write("root_ca_format", "pem")
        except UnicodeDecodeError:
            rootca = Path(rootCA).read_bytes()
            namespace.write("root_ca_format", "der")
        namespace.write("root_ca", rootca)
        self.metadata.add_binding(WORKER_NS_NAME_KEY, namespace.id)

    def deploy(self, worker_name: str, file: str) -> str:
        """Deploy the worker in to CLoudflare Edge network.

        Args:
            worker_name (str): Name of worker. This name will be reflected in the worker url.
            file (str): Javascript file of the worker to deploy

        Returns:
            str: Worker url which is deployed in to CLoudflare Edge network
        """
        worker_file = Path(file).resolve(strict=True)
        if self.worker.upload(
            name=worker_name,
            file=worker_file,
            metadata=self.metadata,
        ):
            if self.worker.deploy(worker_name):
                subdomain = self.worker.subdomain.get()
                return f"https://{worker_name}.{subdomain}.workers.dev"

        raise ValueError("Unexpected input error")
