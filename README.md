# tryingOCR

This is a simple example of code in python using pytesseract wrapper which is an OCR (Optical Character Recognition), i. e., a program dedicated to *read* the words in an image.

## Using the program

Follow this steps to use the program on a windows computer.

### Installing

You need to install the following things:

1. Install python3 from: https://www.python.org/downloads/, check installation using:
```
python --version
```
on the command window.

2. Install libraries using pip:
```
pip install numpy
pip install pytesseract
pip install opencv-python
```

3. Install tesseract from https://github.com/UB-Mannheim/tesseract/wiki, add to path (instructions on link) and check installation using:
```
tesseract --version
```
on the command window.

### Running the tests

Open command window in the directory of the project and run:
```
python main.py
```

You can also modify line 5 to acces to other images.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
