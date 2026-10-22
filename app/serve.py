#!/usr/bin/env python3
"""Start a local HTTP server for the Embodied Carbon visualization app."""
import http.server
import socketserver
import os
import webbrowser
import threading
import sys

port = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Server running at http://localhost:{port}")
    print(f"Open http://localhost:{port} in your browser")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
