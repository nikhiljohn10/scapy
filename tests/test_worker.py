import pytest
from scapy.worker import Worker, WorkerData, WORKER_TITLE_KEY, WORKER_FINGERPRINT_KEY, WORKER_CA_URL_KEY
from CloudflareAPI.api.worker import Worker as CFWorker


@pytest.fixture
def worker_data():
    return WorkerData("TEST_TITLE", "TEST_FINGERPRINT", "TEST_URL")


@pytest.fixture
def worker():
    return CFWorker("TEST_ID")


@pytest.fixture
def worker_data_metadata_bindings():
    return [
        dict(name=WORKER_TITLE_KEY, type="plain_text", text="TEST_TITLE"),
        dict(name=WORKER_FINGERPRINT_KEY, type="plain_text", text="TEST_FINGERPRINT"),
        dict(name=WORKER_CA_URL_KEY, type="plain_text", text="TEST_URL"),
    ]


def test_worker_data_class(worker_data):
    assert worker_data.title == "TEST_TITLE", "Worker:title failed"
    assert worker_data.fingerprint == "TEST_FINGERPRINT", "Worker:title failed"
    assert worker_data.url == "TEST_URL", "Worker:title failed"


def test_worker_data_class_metadata(worker, worker_data, worker_data_metadata_bindings):
    metadata = worker_data.get_metadata(worker)
    bindings = metadata.data["bindings"]
    assert bindings == worker_data_metadata_bindings, "Worker.Metadata:binding failed"


# def test_worker(worker_data_metadata_bindings):
#     worker_instance = Worker("TEST_TITLE", "TEST_FINGERPRINT", "TEST_URL")
#     bindings = worker_instance.metadata.data["bindings"]
#     assert bindings == worker_data_metadata_bindings, "Worker.Metadata:binding failed"
