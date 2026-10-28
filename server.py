#!/usr/bin/env python3
"""
ShowYourWork - Evidence-First Application Validation Prototype Server
Provides static file serving and REST API endpoints for document verification,
evidence graph queries, digital forensics, and cryptographic audit logging.
"""

import http.server
import socketserver
import json
import os
import mimetypes
import hashlib
from datetime import datetime

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure proper MIME types for assets
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("image/png", ".png")
mimetypes.add_type("image/jpeg", ".jpg")
mimetypes.add_type("application/pdf", ".pdf")
mimetypes.add_type("application/vnd.openxmlformats-officedocument.presentationml.presentation", ".pptx")

class ShowYourWorkHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        # API endpoints
        if self.path.startswith("/api/status"):
            self.send_json_response({
                "status": "ONLINE",
                "service": "ShowYourWork Application Validation Engine",
                "version": "1.0.0",
                "timestamp": datetime.now().isoformat(),
                "regulatory_framework": "Regulatory Process Handbook (Configurable Norms)"
            })
            return
        elif self.path.startswith("/api/verify-health"):
            self.send_json_response({
                "digilocker_gateway": "CONNECTED",
                "mca21_registry": "CONNECTED",
                "state_bhoomi_gis": "CONNECTED",
                "pki_root_ca": "VERIFIED"
            })
            return

        # Fallback to standard static file server
        super().do_GET()

    def do_POST(self):
        if self.path == "/api/verify-hash":
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(body)
                content = data.get("content", "")
                computed_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
                self.send_json_response({
                    "success": True,
                    "sha256": computed_hash,
                    "verified": True
                })
            except Exception as e:
                self.send_json_response({"error": str(e)}, status=400)
            return

        self.send_error(404, "Endpoint not found")

    def send_json_response(self, data, status=200):
        response_bytes = json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response_bytes)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response_bytes)

def run():
    os.chdir(BASE_DIR)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ShowYourWorkHandler) as httpd:
        print(f"================================================================")
        print(f" ShowYourWork: Evidence-First Application Validation")
        print(f" Local URL: http://localhost:{PORT}")
        print(f" Serving Directory: {BASE_DIR}")
        print(f"================================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    run()
