

import random
import string


class PUTUpload:
    def __init__(self, http_client):
        self.http = http_client
        self.signature = self.generate_signature()

      
        self.paths = [
            "/uploads/",
            "/files/",
            "/images/",
            "/media/",
            "/temp/",
            "/"
        ]

    
    def generate_signature(self):
        return "PUT_" + ''.join(random.choices(string.ascii_uppercase, k=5))

    
    def create_payload(self):
        content = f"<?php echo '{self.signature}'; ?>"
        filename = f"shell_{self.signature}.php"

        return filename, content.encode()

    
    def attempt_put(self, base_url):
        results = []

        filename, content = self.create_payload()

        for path in self.paths:
            upload_url = base_url.rstrip("/") + path + filename

            print(f"[INFO] Trying PUT upload: {upload_url}")

            response = self.http.put(upload_url, data=content)

            if not response:
                continue

           
            if response.status_code in [200, 201, 204]:
                results.append({
                    "url": upload_url,
                    "status": response.status_code,
                    "signature": self.signature
                })

        return results

   
    def run(self, base_url):
        return self.attempt_put(base_url)
