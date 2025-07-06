# Imports
from utils import errbox
import re

# Import the tokens externally.
from TOKEN_TYPES import TOKEN_TYPES

# Tokenization
def tokenize(code):
    tokens = []
    pos = 0
    line = 1
    col = 1
    while pos < len(code):
        match = None
        for type_, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                value = match.group(0)
                if type_ == "NEWLINE":
                    line += 1
                    col = 1
                elif type_ != "SKIP":
                    col += len(value)
                else:
                    tokens.append({
                        "type": type_,
                        "value": value,
                        "line": line,
                        "col": col
                    })
                    col += len(value)
                pos = match.end()
                break
        if not match:
            errbox(f"Syntac Error at {line}|{col}: {code [0]}")
    return tokens
