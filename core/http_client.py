

import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger("UploadHunter")


class HttpClient:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

       
        self.login()

    def login(self):
        login_url = f"{self.base_url}/login.php"

        try:
           
            res = self.session.get(login_url, timeout=self.timeout)

            if not res:
                logger.error("Failed to load login page")
                return

            soup = BeautifulSoup(res.text, "html.parser")

           
            token_input = soup.find("input", {"name": "user_token"})
            user_token = token_input.get("value") if token_input else ""

            if not user_token:
                logger.warning("CSRF token not found (may still work on low security)")

            
            data = {
                "username": "admin",
                "password": "password",
                "Login": "Login",
                "user_token": user_token
            }

            res = self.session.post(login_url, data=data, timeout=self.timeout)

           
            if "Login failed" in res.text or "login.php" in res.url:
                logger.error("Login failed ❌")
            else:
                logger.info("Login successful ✅")

               
                self.session.cookies.set("security", "low")

        except Exception as e:
            logger.error(f"Login error: {e}")

    def get(self, url):
        try:
            return self.session.get(
                url,
                timeout=self.timeout,
                allow_redirects=True
            )
        except Exception as e:
            logger.error(f"GET failed: {url} | {e}")
            return None

    def post(self, url, files=None, data=None):
        try:
            return self.session.post(
                url,
                files=files,
                data=data,
                timeout=self.timeout,
                allow_redirects=True
            )
        except Exception as e:
            logger.error(f"POST failed: {url} | {e}")
            return None

