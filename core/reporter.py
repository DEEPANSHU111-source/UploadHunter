
import json
from jinja2 import Template
from datetime import datetime


def generate(findings, target):
   
    data = {
        "target": target,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_findings": len(findings),
        "findings": findings
    }

    
    with open("reports/report.json", "w") as f:
        json.dump(data, f, indent=4)

    
    html_template = """
    <html>
    <head>
        <title>UploadHunter Report</title>
        <style>
            body { font-family: Arial; margin: 20px; }
            h1 { color: #333; }
            .high { color: red; }
            .medium { color: orange; }
            .low { color: green; }
            .card {
                border: 1px solid #ccc;
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>

        <h1>UploadHunter Scan Report</h1>

        <p><b>Target:</b> {{ target }}</p>
        <p><b>Scan Time:</b> {{ scan_time }}</p>
        <p><b>Total Findings:</b> {{ total_findings }}</p>

        <hr>

        {% for f in findings %}
        <div class="card">
            <p><b>Type:</b> {{ f.type }}</p>
            <p><b>Payload:</b> {{ f.payload }}</p>
            <p><b>Status:</b> {{ f.status }}</p>
            <p><b>Severity:</b> 
                <span class="{{ f.severity | lower }}">{{ f.severity }}</span>
            </p>
            <p><b>URL:</b> {{ f.url }}</p>
            <p><b>Proof:</b> {{ f.proof }}</p>
        </div>
        {% endfor %}

    </body>
    </html>
    """

  
    template = Template(html_template)
    html_output = template.render(**data)

   
    with open("reports/output.html", "w") as f:
        f.write(html_output)

    print("[+] JSON report saved: reports/report.json")
    print("[+] HTML report saved: reports/output.html")
