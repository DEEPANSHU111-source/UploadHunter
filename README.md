# 🚀 UploadHunter

UploadHunter is an automated security testing tool designed to detect **file upload vulnerabilities** in web applications.

It helps security researchers and students identify critical issues like:

* Unrestricted file upload
* MIME type bypass
* Extension bypass
* Content validation bypass (magic bytes)
* SVG-based XSS
* HTTP PUT upload misconfigurations
* Race condition vulnerabilities

---

## 🎯 Features

* 🔍 Detects file upload forms automatically
* 🧠 Generates smart payloads (PHP, SVG, polyglots)
* ⚡ Supports multiple bypass techniques:

  * Extension bypass
  * MIME type spoofing
  * Content validation bypass
* 💀 Advanced attack modules:

  * SVG XSS
  * PUT upload exploitation
  * Race condition attacks
* 📊 Generates reports (JSON + HTML)

---

## 📁 Project Structure

```
UploadHunter/
├── core/        # Engine (crawler, uploader, executor, analyzer)
├── modules/     # Attack modules
├── payloads/    # Payload files and wordlists
├── utils/       # Helper utilities
├── reports/     # Output reports
├── main.py      # Entry point
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/UploadHunter.git
cd UploadHunter
pip install -r requirements.txt
```

---

## 🚀 Usage

```bash
python main.py --url http://target.com
```

(Optional: Use proxy with Burp Suite)

```bash
python main.py --url http://target.com --proxy http://127.0.0.1:8080
```

---

## 🧪 Modules

| Module             | Description                     |
| ------------------ | ------------------------------- |
| Extension Bypass   | Double extension, case bypass   |
| MIME Bypass        | Fake content-type               |
| Content Validation | Magic byte bypass               |
| SVG XSS            | Stored XSS using SVG            |
| PUT Upload         | Direct upload using PUT method  |
| Race Condition     | Timing-based file upload attack |

---

## 📊 Output

Reports are saved in:

```
reports/report.json
reports/report.html
```

---

## ⚠️ Disclaimer

This tool is for **educational and ethical use only**.

Do not use it on systems without permission.

---

## 👨‍💻 Author

* Name: Deepanshu Deswal
* Field: Cybersecurity | Bug Bounty | web security

---

## ⭐ Future Improvements

* AI-based vulnerability detection
* Automatic exploit chaining
* Cloud scanning support
* Integration with other security tools

---

## 🔥 Why UploadHunter?

File upload vulnerabilities can lead to **Remote Code Execution (RCE)** and **critical security breaches**.

UploadHunter automates:

* Detection
* Exploitation
* Verification

Making it easier to find real-world vulnerabilities.
