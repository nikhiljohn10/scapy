# Scapy Manager
Step CA Manager using Python

## Setup

```bash
git clone https://github.com/nikhiljohn10/scapy
cd scapy
pip install --user poetry
poetry update
```

## Demo

```bash
poetry run bash examples/deploy.sh
```

You will be asked to provide a [Cloudflare Token](https://developers.cloudflare.com/api/tokens/create) to upload the worker. The worker will be uploaded to your Cloudflare Account and deployed to Cloudflare Edge Network.

If successully deployed, you will find a url where the demo CA Root certificate and hosted. Install this certificate in systems to access [stepca.nikz.in](https://stepca.nikz.in).

## Python Package

```
pip install scapy-man
```

### Usage

```
scapy deploy --help
```
