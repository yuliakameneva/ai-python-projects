def run(client, url, param, reporter):

    payloads = [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>"
    ]

    for payload in payloads:
        res = client.send(url, params={param: payload})

        if payload in res.text:
            print(f"[XSS] {param} vulnerable")

            reporter.add(
                "XSS",
                param,
                payload,
                "HIGH",
                "Sanitize input and use output encoding"
            )