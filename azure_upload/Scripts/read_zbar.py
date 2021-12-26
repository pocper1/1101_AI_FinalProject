#!d:\program code\python\1101 ai人工智慧導論\期末project\ai_project_group6\azure_upload\scripts\python.exe
from __future__ import print_function

import argparse
import sys

import pyzbar
from pyzbar.pyzbar import decode


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description='Reads barcodes in images, using the zbar library'
    )
    parser.add_argument('image', nargs='+')
    parser.add_argument(
        '-v', '--version', action='version',
        version='%(prog)s ' + pyzbar.__version__
    )
    args = parser.parse_args(args)

    from PIL import Image

    for image in args.image:
        for barcode in decode(Image.open(image)):
            print(barcode.data)


if __name__ == '__main__':
    main()
