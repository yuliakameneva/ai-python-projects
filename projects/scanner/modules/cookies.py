def run(client, url, reporter):

    client.send(url)

    cookies = client.session.cookies

    for c in cookies:
        secure = c.secure
        httponly = "HttpOnly" in str(c)

        if not secure or not httponly:
            reporter.add(
                "Insecure Cookie",
                c.name,
                "-",
                "MEDIUM",
                "Set Secure and HttpOnly flags for cookies"
            )