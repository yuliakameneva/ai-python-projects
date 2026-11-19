from core.scanner import Scanner
from core.http_client import HttpClient

if __name__ == "__main__":
    base_url = "http://localhost"

    client = HttpClient()

    # логін у DVWA
    client.login("http://localhost/login.php", "admin", "password")

    scanner = Scanner(base_url, client)
    scanner.run()