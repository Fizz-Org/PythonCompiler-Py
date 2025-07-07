import os

# Simple box generator.
def box(text, max_width=os.get_terminal_size().columns):
    # Get the terminal size.
    term_size = os.get_terminal_size()
    width = term_size.columns-2
    
    # Handle max width.
    if width > max_width:
        width = max_width
    
    # Colors
    red = "\x1b[31m"
    cr = "\x1b[0m"

    # Top rows.
    out = [red+"Error:"]
    out.append("╭"+"─"*width+"╮")

    # First split text in to sections by the newline identicator (\n),
    sectiones = text.split("\n")
    for section in sectiones:
        lines = [section[i:i+width] for i in range(0, len(section), width)]
        # then split those into lines.
        for line in lines:
            padded = line.ljust(width)
            out.append("│"+red+padded+red+"│")
    
    # Bottom row.
    out.append("╰"+"─"*width+"╯")

    # Return output.
    return "\n".join(out)

def errbox(text):
    print(box(text))
    exit(1)
