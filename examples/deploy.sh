poetry run scapy deploy \
    --name "Example CA" \
    --fingerprint "9c3a092a9e9ccb6bb37836b611d4934ce59116fcdf1d656a08f9ff14e77ea1cb" \
    --root "./examples/data/root_ca.crt" \
    --worker "example-ca" \
    --js "./examples/data/index.js"
