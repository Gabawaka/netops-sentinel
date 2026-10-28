
from flask import Flask, render_template, redirect, url_for, flash
import platform
import re
import socket
import subprocess
from datetime import datetime

app = Flask(__name__)
app.secret_key = "local-development-key-change-later"

# Your actual home-network targets
ROUTER_IP = "192.168.100.1"
PUBLIC_IP = "8.8.8.8"
DNS_HOSTNAME = "google.com"


def check_ping(target):
    """Check whether a device responds to a single ping."""
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", "-w", "1500", target]
    else:
        command = ["ping", "-c", "1", "-W", "2", target]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=4
        )

        output = result.stdout + result.stderr

        if result.returncode == 0:
            match = re.search(r"time[=<]\s*(\d+)\s*ms", output,
                              re.IGNORECASE)
            latency = f"{match.group(1)} ms" if match else "Responded"

            return {
                "status": "Online",
                "latency": latency,
                "details": "Received a ping reply."
            }

        return {
            "status": "No response",
            "latency": "N/A",
            "details": "Ping failed or may be blocked."
        }

    except (subprocess.TimeoutExpired, OSError) as error:
        return {
            "status": "Error",
            "latency": "N/A",
            "details": str(error)
        }


def check_dns(hostname):
    """Check whether a hostname resolves to an IP address."""
    try:
        addresses = socket.getaddrinfo(hostname, None)
        unique_ips = sorted({item[4][0] for item in addresses})

        return {
            "status": "Working",
            "latency": "N/A",
            "details": ", ".join(unique_ips[:4])
        }

    except socket.gaierror:
        return {
            "status": "Failed",
            "latency": "N/A",
            "details": "Could not resolve the hostname."
        }


def run_network_checks():
    """Run all three network diagnostics."""
    return [
        {
            "name": "Home Router",
            "target": ROUTER_IP,
            **check_ping(ROUTER_IP)
        },
        {
            "name": "Public Internet Host",
            "target": PUBLIC_IP,
            **check_ping(PUBLIC_IP)
        },
        {
            "name": "DNS Resolution",
            "target": DNS_HOSTNAME,
            **check_dns(DNS_HOSTNAME)
        }
    ]


@app.route("/", methods=["GET"])
def dashboard():
    return render_template(
        "index.html",
        results=None,
        checked_at=None
    )


@app.route("/check", methods=["POST"])
def check_network():
    results = run_network_checks()
    checked_at = datetime.now().astimezone().strftime(
        "%d %b %Y, %I:%M:%S %p"
    )

    return render_template(
        "index.html",
        results=results,
        checked_at=checked_at
    )


if __name__ == "__main__":
    app.run(debug=True)
