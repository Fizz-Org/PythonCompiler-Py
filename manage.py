# Error boxes.
from utils import errbox

# Title
title = """\x1b[34m
 ______   __     ______     ______        ______   __  __     ______   __  __     ______     __   __
/\\  ___\\ /\\ \\   /\\___  \\   /\\___  \\      /\\  == \\ /\\ \\_\\ \\   /\\__  _\\ /\\ \\_\\ \\   /\\  __ \\   /\\ \"-.\\ \\
\\ \\  __\\ \\ \\ \\  \\/_/  /__  \\/_/  /__     \\ \\  _-/ \\ \\____ \\  \\/_/\\ \\/ \\ \\  __ \\  \\ \\ \\/\\ \\  \\ \\ \\-.  \\
 \\ \\_\\    \\ \\_\\   /\\_____\\   /\\_____\\     \\ \\_\\    \\/\\_____\\    \\ \\_\\  \\ \\_\\ \\_\\  \\ \\_____\\  \\ \\_\\\\\"\\_\\
  \\/_/     \\/_/   \\/_____/   \\/_____/      \\/_/     \\/_____/     \\/_/   \\/_/\\/_/   \\/_____/   \\/_/ \\/_/                                                                                               
 ______     ______     __    __     ______   __     __         ______     ______
/\\  ___\\   /\\  __ \\   /\\ \"-./  \\   /\\  == \\ /\\ \\   /\\ \\       /\\  ___\\   /\\  == \\
\\ \\ \\____  \\ \\ \\/\\ \\  \\ \\ \\-./\\ \\  \\ \\  _-/ \\ \\ \\  \\ \\ \\____  \\ \\  __\\   \\ \\  __<
 \\ \\_____\\  \\ \\_____\\  \\ \\_\\ \\ \\_\\  \\ \\_\\    \\ \\_\\  \\ \\_____\\  \\ \\_____\\  \\ \\_\\ \\__\\
  \\/_____/   \\/_____/   \\/_/  \\/_/   \\/_/     \\/_/   \\/_____/   \\/_____/   \\/_/ /_/
\x1b[32m(Python Edition)\x1b[0m

Made by \x1b[34mFizz\x1b[0m.
\x1b[33mhttps://github.org/fizz-org\x1b[0m
"""
print(title)

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
    print("\x1b[31mStandard\x1b[0m mode selected...\n")
    print(f"Reading \x1b[33m{filepath}\x1b[0m...\n")
    try:
        with open(filepath, "r") as file:
            code = file.read()
    except Exception as e:
        errbox("Error while reading file: " + str(e))

    # Import the lexer (lexer.py).
    from lexer import tokenize
    print("Tokenizing code...\n")
    tc = tokenize(code)
    return tc

if mode:
    print("Different modes not availlable yet!")
else:
    tc = standard(filepath)
    print(tc)

print(f"Compilation of \x1b[33m{filepath}\x1b[0m complete.")
