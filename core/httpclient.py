import requests

class HttpClient:
    def __init__(self, base_url, cookies=None, headers=None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

        if cookies:
            self.session.cookies.update(cookies)

        if headers:
            self.session.headers.update(headers)

    def post_file(self, endpoint, file_field, file_name, file_bytes, content_type):
        url = self.base_url + endpoint

        files = {
            file_field: (file_name, file_bytes, content_type)
        }

        response = self.session.post(url, files=files, timeout=10)
        return response
