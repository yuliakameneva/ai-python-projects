from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_forms(client, url):
    forms = []
    try:
        res = client.send(url)
        soup = BeautifulSoup(res.text, "html.parser")

        for form in soup.find_all("form"):
            inputs = []

            for inp in form.find_all("input"):
                name = inp.get("name")
                input_type = inp.get("type")

                if name and input_type not in ["hidden", "submit"]:
                    inputs.append(name)

            forms.append({
                "url": url,
                "action": form.get("action"),
                "method": form.get("method", "get").lower(),
                "inputs": inputs
            })

    except Exception as e:
        print(f"[Crawler error] {e}")

    return forms


def crawl(client, base_url):
    print("[+] Crawling...")

    urls = [
        urljoin(base_url, "/vulnerabilities/sqli/"),
        urljoin(base_url, "/vulnerabilities/xss_r/"),
        urljoin(base_url, "/vulnerabilities/fi/"),
        urljoin(base_url, "/vulnerabilities/exec/")
    ]

    all_forms = []

    for url in urls:
        print(f"[+] Scanning {url}")
        forms = extract_forms(client, url)
        all_forms.extend(forms)

    print(f"[+] Found {len(all_forms)} forms")
    return all_forms