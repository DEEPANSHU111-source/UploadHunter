

from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Crawler:
    def __init__(self, client, base_url):
        self.client = client
        self.base_url = base_url
        self.visited = set()

    def fetch_page(self, url):
        try:
            response = self.client.get(url)
            return response.text if response else None
        except Exception as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
            return None

    def extract_forms(self, html, url):
        soup = BeautifulSoup(html, "html.parser")
        forms = []

        for form in soup.find_all("form"):
            form_details = {}


            action = form.get("action")
            action = urljoin(url, action) if action else url

         
            method = form.get("method", "post").lower()

           
            file_input = form.find("input", {"type": "file"})
            if not file_input:
                continue

            inputs = []
            for input_tag in form.find_all("input"):
                inputs.append({
                    "type": input_tag.get("type", "text"),
                    "name": input_tag.get("name")
                })

            form_details["action"] = action
            form_details["method"] = method
            form_details["inputs"] = inputs
            form_details["file_input"] = file_input.get("name")

            forms.append(form_details)

        return forms

    def crawl(self):
        print(f"[*] Crawling {self.base_url}")

        html = self.fetch_page(self.base_url)
        if not html:
            return []

        forms = self.extract_forms(html, self.base_url)

        print(f"[INFO] Found {len(forms)} upload form(s)")
        return forms
