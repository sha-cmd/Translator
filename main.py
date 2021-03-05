# -*- coding: utf-8 -*-
"""PyTranslator"""

"""
Created on Wed Mar  3 01:25:07 2021

Translate docx, doc and pdf files from any spell to french 
into a text file.

@author: romain Boyrie
"""

VERSION = "0.0.1"

import io
import os
import tempfile
from glob import glob
from pdf2image import convert_from_path
from pygoogletranslation import Translator


def find_ext(dr, ext):
    return glob(os.path.join(dr, "*.{}".format(ext)))

def traduction(dr, ext, lg):
    """Traduction of files

            :param dr: The source directory

            :param ext : The file extension

            :param lg : The destination language

            Basic usage:
                >>> traduction('.', 'pdf', 'fr')
                >>> traduction('.', 'docx', 'fr')
                >>> traduction('.', 'doc', 'fr')

    """
    # If it is a pdf, we convert it in jpg, then apply tesseract (ocr) on it, next translating it
    if ext == 'pdf':
        for filename in find_ext(dr, ext):
            with tempfile.TemporaryDirectory() as path:
                images_from_path = convert_from_path(filename)
                base_filename = os.path.splitext(os.path.basename(filename))[0]
                save_dir = '.'
                for idx, page in enumerate(images_from_path):
                    page.save(os.path.join(save_dir, base_filename + '_' + str(idx) + '.jpg'), 'JPEG')

        # Affecting new values for variables
        dr, ext = '.', 'jpg'
        # Translate by ocr
        for filename in find_ext(dr, ext):
            translator = Translator()
            result = translator.bulktranslate(filename, dest=lg)
            complete_name = (filename + ".txt")  # Output files containing traduction

            # Save it on the disk
            with io.open(complete_name, "w", encoding="utf-8") as f:
                f.write(result.text)
                f.close()

    else:
        # Translate some files
        for filename in find_ext(dr, ext):
            translator = Translator()
            result = translator.bulktranslate(filename, dest=lg)
            complete_name = (filename + ".txt")  # Output files containing traduction

            # Save it on the disk
            with io.open(complete_name, "w", encoding="utf-8") as f:
                f.write(result.text)
                f.close()

def main():
    print('Program of traduction from any spell to french in one click')
    traduction('.', 'docx', 'fr')
    traduction('.', 'pdf', 'fr')
    traduction('.', 'doc', 'fr')


if __name__ == '__main__':
    main()
