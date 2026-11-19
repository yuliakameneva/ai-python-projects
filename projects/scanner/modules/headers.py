def run(client, url, reporter):

    res = client.send(url)

    required = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options"
    ]

    for h in required:
        if h not in res.headers:
            print(f"[Headers] Missing {h}")

            reporter.add(
                "Missing Header",
                h,
                "-",
                "MEDIUM",
                f"Add HTTP header: {h} to improve security"
            )