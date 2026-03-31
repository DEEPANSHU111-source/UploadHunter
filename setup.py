from setuptools import setup, find_packages

setup(
    name="UploadHunter",
    version="1.0",
    author="Deepanshu Deswal",
    description="Advanced File Upload Vulnerability Scanner",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "uploadhunter=main:main"
        ]
    },
    python_requires=">=3.8",
)
