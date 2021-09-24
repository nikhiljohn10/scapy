Test commands for Multipass
===========================

```bash
sudo apt update && \
sudo apt install python3-pip -y && \
pip install click click_completion cloudflare-api poetry && \
export PATH=$PATH:$(realpath ~/.local/bin) && \
git clone https://github.com/nikhiljohn10/scapy && \
cd scapy && poetry update

git pull && pip uninstall scapy-man -y && \
poetry run make build && \
pip install dist/scapy_man-0.3.1-py3-none-any.whl && \
scapy -c && . ~/.bash_completion

pip uninstall scapy-man -y && cd .. && rm -rf scapy && clear
```
