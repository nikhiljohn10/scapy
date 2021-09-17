# Scapy Manager (scapy-man)
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

```bash
pip install scapy-man
```

#### Troubleshooting

 - If `scapy` not found: `export PATH=$PATH:$(realpath ~/.local/bin)`
 - If `pip` not found: `sudo apt install python3-pip`
 - If `python3-pip` not found: `sudo apt update`

## Usage with Step CA

```bash
INSTALLATION_PATHS=$(scapy get step all -p)
sudo dpkg -i $INSTALLATION_PATHS
scapy gen passwords
scapy gen worker

export CA_NAME="Scapy CA"
export CA_DNS="stepca.local,localhost"
step ca init \
--name "$CA_NAME" \
--dns "$CA_DNS" \
--address ":443" \
--provisioner admin \
--password-file $(scapy path password root) \
--provisioner-password-file $(scapy path password provisioner)

step crypto change-pass $(scapy path key intermediate) -f \
--password-file $(scapy path password root) \
--new-password-file $(scapy path password intermediate)

export FINGERPRINT=$(step certificate fingerprint $(scapy path cert root))
scapy deploy --worker scapy --js worker.js

sudo setcap CAP_NET_BIND_SERVICE=+eip $(which step-ca)
step-ca $(scapy path config ca) --password-file $(scapy path password intermediate)
```

In the above commands,
 - Generate a password and store in step path
 - Generate a basic worker file
 - Export `CA_NAME` variable with CA Name
 - Generate PKI using Step CA
 - Export `FINGERPRINT` variable with fingerprint of Root Certificate
 - Deploy worker `scapy` with `worker.js` as script file.
