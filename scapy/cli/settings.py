#!/usr/bin/env python3
"""Scapy CLI Settings."""

from pathlib import Path

# Step path
STEP_PATH = (Path.home() / ".step").resolve()

# Default root ca file location
DEFAULT_ROOT_CA_FILE = (STEP_PATH / "certs/root_ca.crt").resolve()

# Default worker file location
DEFAULT_WORKER_FILE = Path("./worker.js").resolve()
