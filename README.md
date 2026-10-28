NetOps Sentinel

A Python-based network monitoring and IT infrastructure diagnostics dashboard.

NetOps Sentinel is a local web application built with Python and Flask to help monitor basic network connectivity. It checks router reachability, public internet-host connectivity, and DNS resolution through a simple web dashboard.

This project is part of my hands-on learning portfolio in programming, networking, IT infrastructure, and technical support.

Features

Router monitoring: Test connectivity to a local network gateway.

Internet reachability: Check whether a public IP address responds to ping.

DNS diagnostics: Resolve domain names and display returned IP addresses.

Response-time reporting: Display ping latency when available.

Web dashboard: View diagnostic results in a clean, responsive interface.

Local execution: Run the application on a Windows computer without paid cloud services.

Technology Stack

Python

Flask

HTML5

CSS3

Git and GitHub

Windows Command Prompt

How It Works

The application performs three checks:

Router connectivity: Sends a ping to the configured local gateway.

Public host connectivity: Sends a ping to a public IP address, 8.8.8.8.

DNS resolution: Uses Python's socket library to resolve google.com.

The results are displayed on the dashboard when a user runs the checks.

Note: A failed ping does not necessarily mean a device or internet connection is unavailable. Some networks block ICMP traffic. DNS resolution and ping tests also do not guarantee that every website or internet service is working.

Requirements

Windows, macOS, or Linux

Python 3.10 or later

Git

An internet connection for the public connectivity and DNS tests

Installation

1. Clone the repository

git clone https://github.com/Gabawaka/netops-sentinel.git
cd netops-sentinel

2. Create a virtual environment

On Windows:

py -m venv .venv
.venv\Scripts\activate

On macOS or Linux:

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

python -m pip install -r requirements.txt

4. Run the application

python app.py

Open the following address in your browser:

http://127.0.0.1:5000

Click Run network checks to display the latest diagnostic results.

Configuration

The initial version uses these monitoring targets:

Check

Target

Home router

192.168.100.1

Public internet host

8.8.8.8

DNS resolution

google.com

These are the targets used in my home lab. The router IP may need to be changed to match another network.

Project Structure

netops-sentinel/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css

Current Limitations

Checks run when requested rather than continuously in the background.

Results are not yet saved to a database.

The application does not yet have user authentication.

Ping availability depends on network and firewall configuration.

The current version focuses on basic diagnostics rather than full enterprise monitoring.

Roadmap

Planned improvements include:

Save monitoring results in SQLite.

Display historical availability and response times.

Add configurable device inventory.

Monitor local CPU, memory, and disk usage.

Introduce IT helpdesk ticket management.

Add automated tests.

Improve configuration and production security.

Learning Objectives

This project provides practical experience with:

Python programming and web development.

TCP/IP networking fundamentals and IP addressing.

Network diagnostics and troubleshooting.

HTML, CSS, and responsive dashboards.

Git version control and GitHub collaboration.

Database integration and automated testing as the project evolves.

Author

Gabriel Wambua

GitHub: @Gabawaka

NetOps Sentinel is a learning and portfolio project. It is not intended to replace enterprise-grade network monitoring or security tools.