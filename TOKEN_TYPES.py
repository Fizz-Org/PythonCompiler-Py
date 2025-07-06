TOKEN_TYPES = [
    # --- Keywords ---
    ("DEF",       r"\bdef\b"),
    ("RETURN",    r"\breturn\b"),
    ("IF",        r"\bif\b"),
    ("ELSE",      r"\belse\b"),
    ("ELIF",      r"\belif\b"),
    ("WHILE",     r"\bwhile\b"),
    ("FOR",       r"\bfor\b"),
    ("IN",        r"\bin\b"),
    ("BREAK",     r"\bbreak\b"),
    ("CONTINUE",  r"\bcontinue\b"),
    ("IMPORT",    r"\bimport\b"),
    ("FROM",      r"\bfrom\b"),
    ("AS",        r"\bas\b"),
    ("PASS",      r"\bpass\b"),
    ("CLASS",     r"\bclass\b"),
    ("AND",       r"\band\b"),
    ("OR",        r"\bor\b"),
    ("NOT",       r"\bnot\b"),
    ("TRUE",      r"\bTrue\b"),
    ("FALSE",     r"\bFalse\b"),
    ("NONE",      r"\bNone\b"),

    # --- Literals ---
    ("STRING",    r'"([^"\\]|\\.)*"'),   # simple string support
    ("NUMBER",    r"\d+(\.\d+)?"),

    # --- Identifiers ---
    ("IDENT",     r"[a-zA-Z_][a-zA-Z0-9_]*"),

    # --- Operators ---
    ("EQ",        r"=="),
    ("NE",        r"!="),
    ("LE",        r"<="),
    ("GE",        r">="),
    ("LT",        r"<"),
    ("GT",        r">"),
    ("PLUS",      r"\+"),
    ("MINUS",     r"-"),
    ("MULT",      r"\*"),
    ("DIV",       r"/"),
    ("MOD",       r"%"),
    ("ASSIGN",    r"="),
    ("POW",       r"\*\*"),

    # --- Delimiters ---
    ("LPAREN",    r"\("),
    ("RPAREN",    r"\)"),
    ("LBRACE",    r"\{"),
    ("RBRACE",    r"\}"),
    ("LBRACKET",  r"\["),
    ("RBRACKET",  r"\]"),
    ("COLON",     r":"),
    ("DOT",       r"\."),
    ("COMMA",     r","),
    ("SEMICOLON", r";"),

    # --- Misc ---
    ("NEWLINE",   r"\n"),
    ("COMMENT",   r"#.*"),
    ("SKIP",      r"[ \t]+"),
]

