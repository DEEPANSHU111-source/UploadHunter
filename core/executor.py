

import time
from concurrent.futures import ThreadPoolExecutor
import logging

logger = logging.getLogger("UploadHunter")


def verify_upload(client, base_url, filename):
    """
    Try to access uploaded file at common locations
    """
    paths = [
        f"{base_url}/uploads/{filename}",
        f"{base_url}/images/{filename}",
        f"{base_url}/{filename}",
        f"{base_url}/files/{filename}"
    ]

    for url in paths:
        try:
            res = client.get(url)

            if res and res.status_code == 200:
                return url

        except Exception as e:
            logger.debug(f"Verification error for {url}: {e}")
            continue

    return None


def process_result(client, base_url, result):
    filename = result.get("filename")

    if filename:
        verified_url = verify_upload(client, base_url, filename)

        if verified_url:
            logger.info(f"[+] File accessible: {verified_url}")

            result["verified"] = True
            result["exploit_url"] = verified_url

           
            try:
                res = client.get(verified_url)
                if res and "UPLOAD_HUNTER_RCE" in res.text:
                    logger.info(f"[🔥] RCE CONFIRMED: {verified_url}")
                    result["rce"] = True
                    result["severity"] = "Critical"
                else:
                    result["rce"] = False
                    result["severity"] = "High"
            except:
                result["rce"] = False
                result["severity"] = "High"

        else:
            result["verified"] = False
            result["rce"] = False
            result["severity"] = "Low"

    return result

def run_modules(client, base_url, uploader, modules, threads=1):
    """
    Run all modules with threading + verification
    """
    all_results = []

    for module in modules:
        logger.info(f"Running module: {module.__name__}")

        try:
            results = module(uploader)

          
            with ThreadPoolExecutor(max_workers=threads) as executor:
                processed_results = list(
                    executor.map(
                        lambda r: process_result(client, base_url, r),
                        results
                    )
                )

            all_results.extend(processed_results)

        except Exception as e:
            logger.error(f"Module {module.__name__} failed: {e}")

    return all_results
