

class Config:
 
    TIMEOUT = 10
    THREADS = 10

  
    PROXY = None
   
    # PROXY = "http://127.0.0.1:8080"

    
    HEADERS = {
        "User-Agent": "UploadHunter/1.0",
        "Accept": "*/*"
    }

    PAYLOADS_DIR = "payloads/"
    POLYGLOTS_DIR = "payloads/polyglots/"
    SVG_XSS_DIR = "payloads/svg_xss/"
    RACE_DIR = "payloads/race/"

    EXTENSIONS_FILE = "payloads/extensions.txt"
    MIME_TYPES_FILE = "payloads/mime_types.json"

   
    REPORT_JSON = "reports/report.json"
    REPORT_HTML = "reports/report.html"

   
    VERIFY_SSL = False
    FOLLOW_REDIRECTS = True

    
    DEBUG = True
