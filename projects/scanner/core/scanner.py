from core.reporter import Reporter
from utils.crawler import crawl
from modules import sqli, xss, lfi, traversal, cmdi, headers, cookies


class Scanner:

    def __init__(self, url, client):
        self.url = url
        self.client = client
        self.reporter = Reporter()

    def run(self):
        print("[+] Crawling...")

        forms = crawl(self.client, self.url)

        print(f"[+] Found {len(forms)} forms")

        for form in forms:
            url = form["url"]

            for param in form["inputs"]:
                print(f"[+] Testing {param} at {url}")

                sqli.run(self.client, url, param, self.reporter)
                xss.run(self.client, url, param, self.reporter)
                lfi.run(self.client, url, param, self.reporter)
                traversal.run(self.client, url, param, self.reporter)
                cmdi.run(self.client, url, param, self.reporter)

        headers.run(self.client, self.url, self.reporter)
        cookies.run(self.client, self.url, self.reporter)

        print("\n[DEBUG RESULTS]")
        print(self.reporter.results)

        self.reporter.generate_html()

        print("[+] Scan complete")