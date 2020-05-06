# TODO: Use regexes

"""
Matches regex search strings to the resulting font.
inspiration taken from https://www.markdownguide.org/basic-syntax/.

Limitations:
- Can't format across lines :(
- Many bugs probably...oh well
"""

FORMATTING_RULES = {
    # headings 1, 2, and 3
    "#": "Times 24 bold",
    "##": "Times 20 bold",
    "###": "Times 16 bold",
    # italic, bold, bold italic
    "*": "Helvetica 14 italic",
    "**": "Helvetica 14 bold",
    "***": "Helvetica 14 bold italic",
    # underline
    "&&": "Helvetica 14 underline",
    # code-looking stuff
    "`": "Consolas 14"
}

FORMATTING_REGEXES = [
    # matches "#heading#", "##heading##", and "###heading###"
    r"([#]+)(.+?)([#]+)",
    # matches "*italic*", "**bold**", and "***bold italic***"
    r"([\*]+)(.+?)([\*]+)",
    # matches "&&underline&&"
    r"([&]{2})(.+?)([&]{2})",
    # matches "`code`"
    r"([`])(.+?)([`])"]

DEFAULT_FONT = ("Helvetica", "14")
