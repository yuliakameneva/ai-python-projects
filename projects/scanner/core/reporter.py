from html import escape


class Reporter:

    def __init__(self):
        self.results = []

    def add(self, vuln_type, param, payload, risk, recommendation):
        self.results.append({
            "type": vuln_type,
            "param": param,
            "payload": payload,
            "risk": risk,
            "recommendation": recommendation
        })

    def generate_html(self):

        high = sum(1 for r in self.results if r["risk"] == "HIGH")
        medium = sum(1 for r in self.results if r["risk"] == "MEDIUM")
        low = sum(1 for r in self.results if r["risk"] == "LOW")

        total = len(self.results) if self.results else 1

        html = f"""
        <html>
        <head>
        <title>Security Scan Report</title>
        <style>
            body {{ font-family: Arial; background: #0f172a; color: #e2e8f0; }}
            h1 {{ color: #38bdf8; }}
            table {{ border-collapse: collapse; width: 100%; margin-top:20px; }}
            th, td {{ padding: 10px; border: 1px solid #334155; text-align: left; }}
            th {{ background: #1e293b; }}

            .HIGH {{ background-color: #7f1d1d; }}
            .MEDIUM {{ background-color: #78350f; }}
            .LOW {{ background-color: #14532d; }}

            .card {{
                display: inline-block;
                padding: 15px;
                margin: 10px;
                border-radius: 10px;
                background: #1e293b;
            }}
        </style>
        </head>
        <body>

        <h1> Web Vulnerability Scan Report</h1>

        <div class="card">Total: {total}</div>
        <div class="card">HIGH: {high}</div>
        <div class="card">MEDIUM: {medium}</div>
        <div class="card">LOW: {low}</div>

        <table>
        <tr>
            <th>Type</th>
            <th>Parameter</th>
            <th>Payload</th>
            <th>Risk</th>
            <th>Recommendation</th>
        </tr>
        """

        for r in self.results:
            html += f"""
            <tr class="{r['risk'] if r['risk'] in ('HIGH','MEDIUM','LOW') else ''}">
                <td>{escape(str(r['type']))}</td>
                <td>{escape(str(r['param']))}</td>
                <td>{escape(str(r['payload']))}</td>
                <td>{escape(str(r['risk']))}</td>
                <td>{escape(str(r['recommendation']))}</td>
            </tr>
            """

        html += "</table></body></html>"

        with open("report.html", "w", encoding="utf-8") as f:
            f.write(html)