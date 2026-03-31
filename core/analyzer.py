import re
import logging


class ResponseAnalyzer:
    def __init__(self):
       
        self.success_patterns = [
            r"uploaded successfully",
            r"file uploaded",
            r"successfully uploaded",
            r"image uploaded",
            r"upload success",
        ]

        
        self.failure_patterns = [
            r"upload failed",
            r"error uploading",
            r"not allowed",
            r"invalid file",
            r"permission denied",
        ]

       
        self.execution_patterns = [
            r"uid=\d+",
            r"gid=\d+",
            r"root:",
            r"www-data",
            r"command not found",
        ]

    def analyze_upload_response(self, response_text):
        """
        Analyze upload response to determine success/failure
        """

        text = response_text.lower()

        for pattern in self.success_patterns:
            if re.search(pattern, text):
                return {
                    "status": "success",
                    "reason": f"Matched success pattern: {pattern}"
                }

        for pattern in self.failure_patterns:
            if re.search(pattern, text):
                return {
                    "status": "failed",
                    "reason": f"Matched failure pattern: {pattern}"
                }

        return {
            "status": "unknown",
            "reason": "No clear pattern matched"
        }

    def analyze_execution_response(self, response_text):
        """
        Detect if uploaded file is executing (RCE detection)
        """

        text = response_text.lower()

        for pattern in self.execution_patterns:
            if re.search(pattern, text):
                return {
                    "executed": True,
                    "evidence": pattern
                }

        return {
            "executed": False,
            "evidence": None
        }

    def analyze_status_code(self, status_code):
        """
        Basic HTTP status analysis
        """

        if status_code == 200:
            return "OK"
        elif status_code == 403:
            return "Forbidden"
        elif status_code == 404:
            return "Not Found"
        elif status_code == 500:
            return "Server Error"
        else:
            return f"Status {status_code}"

    def full_analysis(self, upload_response, execution_response=None):
        """
        Combined smart analysis
        """

        result = {}

      
        upload_result = self.analyze_upload_response(upload_response)
        result["upload"] = upload_result

       
        if execution_response:
            exec_result = self.analyze_execution_response(execution_response)
            result["execution"] = exec_result

            if exec_result["executed"]:
                result["final_status"] = "CRITICAL - RCE Achieved 🚨"
            elif upload_result["status"] == "success":
                result["final_status"] = "Upload Success but No Execution"
            else:
                result["final_status"] = "Upload Failed"

        else:
            result["final_status"] = upload_result["status"]

        return result
