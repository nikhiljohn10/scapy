# Scapy Manager (scapy-man)

[![](https://img.shields.io/pypi/status/scapy-man)](https://pypi.org/project/scapy-man/) [![](https://img.shields.io/pypi/v/scapy-man)](https://pypi.org/project/scapy-man/) [![](https://img.shields.io/pypi/pyversions/scapy-man)](https://pypi.org/project/scapy-man/) [![](https://readthedocs.org/projects/scapy-manager/badge/?version=latest)](https://scapy-manager.readthedocs.io/en/latest/?badge=latest) [![](https://www.codefactor.io/repository/github/nikhiljohn10/scapy/badge)](https://www.codefactor.io/repository/github/nikhiljohn10/scapy) [![](https://img.shields.io/github/license/nikhiljohn10/scapy)](https://github.com/nikhiljohn10/scapy/blob/main/LICENSE)

Step CA Manager using Python

Documenation: [scapy.nikz.in](https://scapy.nikz.in)

## Setup

```bash
git clone https://github.com/nikhiljohn10/scapy
cd scapy
pip install poetry
poetry update
```

## Demo

```bash
poetry run bash examples/deploy.sh
```

You will be asked to provide a [Cloudflare Token](https://developers.cloudflare.com/api/tokens/create) to upload the worker. The worker will be uploaded to your Cloudflare Account and deployed to Cloudflare Edge Network.

If successully deployed, you will find a url where the demo CA Root certificate and hosted. Install this certificate in systems to access [stepca.nikz.in](https://stepca.nikz.in).

## Python Package

```bash
pip install scapy-man
```

#### Completion

```bash
scapy --completion
```
This command will install the shell completion. To activate the shell completion in currently working shell, run `. ~/.bash_completion` or `source ~/.bash_completion`.

#### Troubleshooting

 - If `scapy` not found: `export PATH=$PATH:$(realpath ~/.local/bin)`
 - If `pip` not found: `sudo apt install python3-pip -y`
 - If `python3-pip` not found: `sudo apt update`

## Usage with Step CA

```bash
# Download deb packages
INSTALLATION_PATHS=$(scapy get step all -p)

# Install deb packages downloaded
sudo dpkg -i $INSTALLATION_PATHS

# Generate a password
scapy gen passwords

# Generate a basic worker file
scapy gen worker

# Export CA_NAME variable with CA Name
export CA_NAME="Scapy CA"

# Export domain names to use with this CA
export CA_DNS="$(hostname).local,localhost"

# Generate a new certificate authority
step ca init \
--name "$CA_NAME" \
--deployment-type standalone \
--dns "$CA_DNS" \
--address ":443" \
--provisioner admin \
--password-file $(scapy path password root) \
--provisioner-password-file $(scapy path password provisioner)

# Change default password of intermediate CA private key
step crypto change-pass $(scapy path key intermediate) -f \
--password-file $(scapy path password root) \
--new-password-file $(scapy path password intermediate)

# Export the FINGERPRINT variable with fingerprint of Root CA Certificate
export FINGERPRINT=$(step certificate fingerprint $(scapy path cert root))

# Deploy the Root CA and Fingerprint with CA URL to Cloudflare Edge server
scapy deploy --worker scapy --js worker.js

# Enable previllaged prot access for non-root users
sudo setcap CAP_NET_BIND_SERVICE=+eip $(which step-ca)

# Start Step CA server
step-ca $(scapy path config ca) --password-file $(scapy path password intermediate)
```

## Commandline Interface

![Scapy CLI](https://raw.githubusercontent.com/nikhiljohn10/scapy/main/docs/_static/scapy-commands.png)
