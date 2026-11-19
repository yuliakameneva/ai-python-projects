def get_sqli_payloads():
    return [
        "' OR 1=1--",
        "' OR '1'='1"
    ]

def get_xss_payloads():
    return [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>"
    ]