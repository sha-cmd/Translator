# Translator
Unlimited traduction of files from any language to french in one operation.

## How to install

Download the sources from this repository, or clone it with git command.

Inside your program directory, create a virtual environment with Python :
`python -m venv venv`

Then activate the script in `[Path_to_the_program]/venv/Script/` :
Under Windows launch `activate.bat` batch file, or the script named without extension `activate` if you are under Unix’Like systems.

Install all requirements (verify your virtual environnement is activate):

`(venv) [Path_to_the_program]: pip install -r requirements.txt`

You must have installed [Tesseract](https://tesseract-ocr.github.io/tessdoc/Home.html) on your system and put its directory into the Path of your system variables, in order to indicate the direction toward the directory containing the executable tesseract.

## License

Translator is licensed under the MIT License. The terms are as follows:

:: MIT License

Copyright (c) 2021 Sha-cmd

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
