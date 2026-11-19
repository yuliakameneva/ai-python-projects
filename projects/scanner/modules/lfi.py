from core.analyzer import ResponseAnalyzer

payloads = [
    "../../etc/passwd",
    "../../../../etc/passwd"
]


def run(client, url, param, reporter):
    baseline = client.send(url, params={param: "test"}).text

    for payload in payloads:
        res = client.send(url, params={param: payload}).text

        if "root:x:" in res or \
           ResponseAnalyzer.is_different(baseline, res):

            print(f"[LFI] {param} vulnerable")

            reporter.add(
                "Local File Inclusion",
                param,
                payload,
                "HIGH",
                "Restrict file access and validate file paths"
            )