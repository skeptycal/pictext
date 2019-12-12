#!/usr/bin/env python3

import os

from setuptools import setup


README = ""

if os.path.isfile("README.md"):
    with open("README.md") as f:
        README = f.read()

setup(
    name="pictext",
    version=tessy.VERSION,
    author="skeptycal",
    author_email="skeptycal@gmail.com",
    url="https://github.com/skeptycal/pictext",
    license="MIT",
    description="A Python wrapper for OpenCV.",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords="python tesseract opencv cv2 ocr",
    packages=["pictext"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
)
