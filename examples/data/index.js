/*
    Scapy Manager (scapy)
    * Author: Nikhil John
    * Source: https://github.com/nikhiljohn10/scapy
    * License: MIT
*/

function get_html(body) {
    return `<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootswatch@5.1.1/dist/simplex/bootstrap.min.css"
    integrity="sha256-q4d6dBEE09GKG+jEE5jQ0gxJR/JNMcwOhpad0fbNkhc=" crossorigin="anonymous">
    <title>${CA_TITLE}</title>
</head>

<body>
    <div class="container">
        <div class="row justify-content-md-center">
            ${body}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.8/clipboard.min.js"
    integrity="sha512-sIqUEnRn31BgngPmHt2JenzleDDsXwYO+iyvQ46Mw6RL+udAUZj2n/u/PGY80NxRxynO7R9xIGx5LEzw4INWJQ=="
    crossorigin="anonymous"></script>
    <script>
    (function () {
        /* Show current year in copyright */
        document.getElementById('currentYear').innerHTML = new Date().getFullYear();
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
        })
        /* Clipboard JS */
        const cb = new ClipboardJS('.btn-clipboard', {
        target: function (trigger) {
            return trigger.previousElementSibling
        }
        })
        cb.on('success', function (event) {
        const bstt = bootstrap.Tooltip.getInstance(event.trigger);
        event.trigger.setAttribute('data-bs-original-title', 'Copied!')
        bstt.show()
        event.trigger.setAttribute('data-bs-original-title', 'Copy to clipboard')
        event.clearSelection()
        })
    })();
    </script>
</body>

</html>` }

function error_page(code, content) {
    return get_html(`
    <div class="col-md-auto">
        <h1>Error <span class="text-primary">${code}</span>: ${content}</h1>
    </div>`)
}

function root_page() {
    return get_html(`
    <div class="col-md-6 col-lg-4">
        <h1 class="text-center my-5">${CA_TITLE}</h1>
        <div class="mb-3">
            <label for="fingerprintField" class="form-label">
            <a href="/fp" class="link-primary text-decoration-none">Fingerprint</a>
            </label>
            <div class="input-group mb-3">
            <input type="text" class="form-control" id="fingerprintField" value="${ROOT_CA_FINGERPRINT}"
                aria-label="Certificate Authority's Root Fingerprint" readonly>
            <button class="btn btn-outline-secondary btn-clipboard" type="button" data-bs-toggle="tooltip"
                data-bs-placement="bottom" title="" data-bs-original-title="Copy to clipboard">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                class="bi bi-clipboard-check" viewBox="0 0 16 16">
                <path fill-rule="evenodd"
                    d="M10.854 7.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 9.793l2.646-2.647a.5.5 0 0 1 .708 0z" />
                <path
                    d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z" />
                <path
                    d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z" />
                </svg>
            </button>
            </div>
        </div>
        <div class="mb-3">
            <label for="caUrlField" class="form-label">
            <a href="/url" class="link-primary text-decoration-none">CA URL</a>
            </label>
            <div class="input-group mb-3">
            <input type="text" class="form-control" id="caUrlField" value="${ROOT_CA_URL}"
                aria-label="Certificate Authority's URL" readonly>
            <button class="btn btn-outline-secondary btn-clipboard" type="button" data-bs-toggle="tooltip"
                data-bs-placement="bottom" title="" data-bs-original-title="Copy to clipboard">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                class="bi bi-clipboard-check" viewBox="0 0 16 16">
                <path fill-rule="evenodd"
                    d="M10.854 7.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 9.793l2.646-2.647a.5.5 0 0 1 .708 0z" />
                <path
                    d="M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z" />
                <path
                    d="M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z" />
                </svg>
            </button>
            </div>
        </div>
        <a href="/root_ca.crt" type="button" class="w-100 btn btn-lg btn-primary my-4">Download Root CA
            Certificate</a>
        <p class="lead">This website is owned and maintained by ${CA_TITLE}. You can download and install our root
            certificate if you are wish to securely connect to services within our organisatoin.</p>
        <p class="text-secondary mb-5">Fingerprint and CA Url are used for bootstrapping in unix based systems.</p>
        <hr />
        <p class="text-center text-muted"><small>Copyright &copy; <span id="currentYear"></span> <a href="https://github.com/nikhiljohn10/scapy">Scapy Manager</a></small>
        </p>
    </div>`)
}

addEventListener("fetch", (event) => {
    event.respondWith(
        handleRequest(event.request).catch(
            (err) => new Response(err.stack, {
                status: 500
            })
        )
    )
})

async function handleRequest(request) {
    const { pathname } = new URL(request.url)
    const html_headers = {
        "Content-Type": "text/html;charset=UTF-8"
    }
    if (pathname.startsWith("/root_ca.crt")) {
        let certificate
        const format = await CA_CERT_STORE.get("root_ca_format")
        if (format == "der") {
            certificate = await CA_CERT_STORE.get("root_ca", "arrayBuffer")
            return new Response(certificate, {
                headers: {
                    "Content-Type": "application/octet-stream"
                }
            })
        }
        certificate = await CA_CERT_STORE.get("root_ca")
        return new Response(certificate, {
            headers: {
                "Content-Type": "application/x-x509-ca-cert"
            }
        })
    }

    if (pathname.startsWith("/fp")) {
        return new Response(ROOT_CA_FINGERPRINT)
    }

    if (pathname.startsWith("/url")) {
        return new Response(ROOT_CA_URL)
    }

    if (pathname == ("/" || "")) {
        return new Response(root_page(), { headers: html_headers })
    }

    return new Response(error_page(404, "Page not found"), {
        status: 404,
        headers: html_headers
    })
}
