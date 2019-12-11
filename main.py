#!/usr/bin/env python3

from pathlib import Path
import cv2
import pytesseract


def main():
    '''
    pyText CLI script main entry point.
    '''
    print(f"open-cv version: {cv2.getVersionString()}")
    print(f"pyTesseract Version: {pytesseract.get_tesseract_version()}")

    p = Path('samples/bitcoin.jpeg')
    filename = p.resolve().as_posix()
    print(filename)
    img = cv2.imread(filename)
    text = pytesseract.image_to_string(img)


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()
