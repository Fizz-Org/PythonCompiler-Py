# Error boxes.
from utils import errbox

# Argument parsing.
import argparse
parser = argparse.ArgumentParser(
    prog="Python Compiler - Python Edition",
    description="A compiler for Python build in Python. Made by Fizz: https://github.com/fizz-org.",
    epilog="Made by Fizz.")
parser.add_argument('filename')
parser.add_argument('-m', '--mode')
args = parser.parse_args()
filepath = args.filename
mode = args.mode

def standard(filepath):
    try:
        with open(filepath, "r") as file:
            code = file.read()
    except Exception as e:
        errbox("Error while reading file: " + str(e))

    # Import the lexer (lexer.py).
    from lexer import tokenize

    tc = tokenize(code)
    return tc

if mode:
    print("Different modes not availlable yet!")
else:
    tc = standard(filepath)
    print(tc)
