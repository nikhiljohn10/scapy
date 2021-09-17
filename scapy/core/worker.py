#!/usr/bin/env python3
"""Cloudflare Worker module to deploy Root certificate."""

from pathlib import Path
from typing import Optional, Union

from CloudflareAPI import Cloudflare
from CloudflareAPI.api import Worker as CFWorker
from CloudflareAPI.dataclass.namespace import Namespace
from CloudflareAPI.exceptions import CFError


class Worker:
    """Cloudflare Worker class which handle the deployment of Root certificate."""

    WORKER_NS_NAME_KEY = "CA_CERT_STORE"
    WORKER_TITLE_KEY = "CA_TITLE"
    WORKER_FINGERPRINT_KEY = "ROOT_CA_FINGERPRINT"
    WORKER_CA_URL_KEY = "ROOT_CA_URL"

    def __init__(self, token: Optional[str] = None) -> None:
        """Initialise the Cloudflare API.

        Args:
            token (str): Optional argument to pass Cloudflare API Token
        """
        self.api = Cloudflare(token=token)
        self.metadata: Optional[CFWorker.Metadata] = None

    def store(self, web_title: str, fingerprint: str, ca_url: str) -> None:
        """Store data to be published.

        Args:
            web_title (str): Title of the Worker
            fingerprint (str): Fingerprint to attach to the worker
            ca_url (str): CA URL to attach to the worker
        """
        self.title, self.fingerprint, self.url = (
            web_title,
            fingerprint,
            ca_url,
        )

    def get_metadata(self, namespace: Namespace) -> None:
        """Generate for the Cloudflare worker.

        Args:
            namespace (CloudflareAPI.dataclass.Namespace): Namespace instance of Cloudflare API.
        """
        self.metadata = self.api.worker.Metadata()
        self.metadata.add_variable(self.WORKER_TITLE_KEY, self.title)
        self.metadata.add_variable(
            self.WORKER_FINGERPRINT_KEY, self.fingerprint
        )
        self.metadata.add_variable(self.WORKER_CA_URL_KEY, self.url)
        self.metadata.add_binding(self.WORKER_NS_NAME_KEY, namespace.id)

    def loadCA(self, rootCA: Union[str, Path]) -> None:
        """Load the CA certificate and write to the Cloudflare KV Namespace.

        Args:
            rootCA (str): Root Certificate file location
        """
        rootca: Optional[Union[bytes, str]] = None
        rootCA_file = Path(rootCA) if not isinstance(rootCA, Path) else rootCA
        try:
            namespace = self.api.store.get_ns(self.WORKER_NS_NAME_KEY)
        except CFError:
            namespace = self.api.store.create(self.WORKER_NS_NAME_KEY)
        try:
            rootca = rootCA_file.read_text()
            namespace.write("root_ca_format", "pem")
        except UnicodeDecodeError:
            rootca = rootCA_file.read_bytes()
            namespace.write("root_ca_format", "der")
        namespace.write("root_ca", rootca)
        self.get_metadata(namespace)

    def deploy(self, name: str, file: Union[str, Path]) -> str:
        """Deploy the worker in to Cloudflare Edge network.

        Args:
            name (str): Name of worker. This name will be reflected in the worker url.
            file (str): Javascript file of the worker to deploy

        Returns:
            str: Worker url which is deployed in to CLoudflare Edge network
        """
        if self.metadata is not None:
            worker_name = name.strip().lower()
            worker_file = (
                Path(file).resolve(strict=True)
                if not isinstance(file, Path)
                else file
            )
            if self.api.worker.upload(
                name=worker_name,
                file=worker_file,
                metadata=self.metadata,
            ):
                if self.api.worker.deploy(worker_name):
                    subdomain = self.api.worker.subdomain.get()
                    return f"https://{worker_name}.{subdomain}.workers.dev"

            raise CFError("Deployment failed")

        raise CFError("Metadata not found")
