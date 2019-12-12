#!/usr/bin/env python3

from pathlib import Path
import cv2
import pytesseract

DEFAULT_TABLE_WIDTH = 79
TOP_TABLE_BORDER = '-' * DEFAULT_TABLE_WIDTH


def check_file(filename: str) -> str:
    """ Verify filename and return posixpath. """
    # p = Path(filename)
    return (p:= Path(filename)).resolve().as_uri()


def img2txt(filename: str) -> str:
    """ Detect and return text from common images. """
    p = Path(filename)
    filename = p.resolve().as_posix()
    img = cv2.imread(filename)
    result = pytesseract.image_to_string(img)
    return result


def load_img():
    """ Read image using OpenCV """
    # Save image in set directory
    # Read RGB image
    img = cv2.imread('g4g.png')

    # Output img with window name as 'image'
    cv2.imshow('image', img)

    # Maintain output window utill
    # user presses a key
    cv2.waitKey(0)

    # Destroying present windows on screen
    cv2.destroyAllWindows()


def print_img(filename: str, debug: bool = False):
    print()
    print(TOP_TABLE_BORDER)
    if debug:
        print(
            f"open-cv: {cv2.getVersionString()}  pyTesseract: {pytesseract.get_tesseract_version()}")
        print(f"filename: {filename}")
        print()
        print(TOP_TABLE_BORDER)
    print(img2txt(filename))
    print(TOP_TABLE_BORDER)


def main():
    '''
    pyText CLI script main entry point.
    Sample text from images...
    '''
    debug = False
    print_img('samples/code.png', debug)
    print_img('samples/breaking.png', debug)
    print_img('samples/bitcoin.jpeg', debug)


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()
