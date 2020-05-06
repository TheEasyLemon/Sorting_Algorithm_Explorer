# private imports
from .wiki_formatting_rules import FORMATTING_RULES, FORMATTING_REGEXES, DEFAULT_FONT


# python imports
import re
import tkinter as tk


class Wiki_Formatter(tk.Text):
    """Handles formatting from a plain .txt file into a disabled Tk.Text
    widget for display.

    Because tk.Text cannot directly handle bold words, italics, or underlining,
    I've implemented a simple markdown language to bridge the gap.
    """

    def __init__(self, name, func_name, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self["font"] = DEFAULT_FONT
        self["wrap"] = "word"
        
        with open(f"Sorting_ALgorithm/wiki/{func_name}.txt", "r") as file:
            contents = file.read()

        self._format(contents)

        # disallow editing, basically turns Text in multi-line Label
        # goes last because it also disables delete/insert
        self.configure(state="disabled")

    def _format(self, contents):
        """(str) => None
        Formats and inserts the text into the tk.Text instance.
        Uses FORMATTING_RULES, which are inspired by Markdown.
        """
        
        # go through each line
        for linenum, line in enumerate(contents.split("\n")):
            # insert the line and newline
            self.insert(tk.END, line + "\n")
            
            matches = []
            
            # finding all matches in a line
            for regex in FORMATTING_REGEXES:
                all_matches = re.findall(regex, line)
                for matchnum, match in enumerate(all_matches):
                    
                    # make sure the match is valid
                    if match[0] == match[2]:
                        self._replace(match, linenum, matchnum)

    
    def _replace(self, match, linenum, matchnum):
        """(Match obj (tuple of str), str, int) => ()
        Modifies the text based on the match object. Deletes
        the Markdown-style text and replaces it with formatted text.
        Does this for a specific line number linenum.

        Each match object must have a unique matchnum, at least within
        the same line. This allows for tags to be unique.
        """
        
        full_match = match[0] + match[1] + match[2]
        full_start = self.get(f"{linenum + 1}.0", f"{linenum + 1}.end").find(full_match)
        full_end = full_start + len(full_match)

        formatted = match[1]
        form_start = full_start
        form_end = form_start + len(formatted)

        # Note: delete and insert use position denoted as (line.index),
        # but line is one-indexed while index is zero-indexed

        # deletes the "##stuff##"
        self.delete(f"{linenum + 1}.{full_start}", f"{linenum + 1}.{full_end}")
        # replaces it with "stuff"
        self.insert(f"{linenum + 1}.{form_start}", formatted)
        
        # adds a tag at "stuff" and formats it
        self.tag_add(f"{linenum + 1}.{matchnum}", f"{linenum + 1}.{form_start}",
                     f"{linenum + 1}.{form_end}")
        self.tag_config(f"{linenum + 1}.{matchnum}", font=FORMATTING_RULES[match[0]])
        

# test driver code
"""
if __name__ == "__main__":
    main = tk.Tk()
    test = Wiki_Formatter("List.sort()", "list_sort")
    test.pack()
    main.mainloop()
"""
