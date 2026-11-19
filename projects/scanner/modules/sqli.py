def run(client, url, param, reporter):

    payloads = ["' OR 1=1--", "' OR '1'='1"]

    baseline = client.send(url, params={param: "test"})
    base_len = len(baseline.text)

    for payload in payloads:
        res = client.send(url, params={param: payload})

        if (
            abs(len(res.text) - base_len) > 20
            or "Welcome" in res.text
            or "admin" in res.text
        ):
            print(f"[SQLi] {param} vulnerable")

            reporter.add(
                "SQL Injection",
                param,
                payload,
                "HIGH",
                "Use prepared statements and parameterized queries"
            )