import argparse
import logging
import requests
from core.uploader import FileUploader

def setup_logger(debug=False):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", level=level)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--threads", type=int, default=5)
    parser.add_argument("--debug", action="store_true")

   
    parser.add_argument("--proxy", help="Proxy (Burp) e.g. http://127.0.0.1:8080")

    args = parser.parse_args()

    setup_logger(args.debug)

    session = requests.Session()

    base_url = args.url.split("/vulnerabilities")[0]

    uploader = FileUploader(
        session=session,
        upload_url=args.url.rstrip("/"),
        file_field="uploaded",
        base_url=base_url,
        threads=args.threads,
        proxy=args.proxy  
    )

    uploader.run_all()

if __name__ == "__main__":
    main()
