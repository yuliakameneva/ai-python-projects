import requests
from bs4 import BeautifulSoup


class HttpClient:
    def __init__(self):
        self.session = requests.Session()

    def login(self, url, username, password):
        # 1. отримуємо сторінку логіну
        res = self.session.get(url)

        soup = BeautifulSoup(res.text, "html.parser")

        # 2. витягуємо CSRF token
        token = soup.find("input", {"name": "user_token"}).get("value")

        # 3. логін з токеном
        res = self.session.post(url, data={
            "username": username,
            "password": password,
            "Login": "Login",
            "user_token": token
        })

        print("[LOGIN] status:", res.status_code)

        # 4. встановлюємо LOW security (теж з токеном)
        sec_page = self.session.get("http://localhost/security.php")
        soup = BeautifulSoup(sec_page.text, "html.parser")
        token = soup.find("input", {"name": "user_token"}).get("value")

        self.session.post("http://localhost/security.php", data={
            "security": "low",
            "seclev_submit": "Submit",
            "user_token": token
        })

    def send(self, url, params=None):
        return self.session.get(url, params=params)