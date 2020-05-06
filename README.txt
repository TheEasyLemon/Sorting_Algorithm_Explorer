# Dawson’s Sorting Algorithm Explorer

---

## Overview

This is an interactive applet that compares, explains, and interactively displays sorting algorithms. The currently implemented algorithms are:

1. Python sorted()
2. List.sort()
3. Insertion Sort
4. Selection Sort
5. Bubble Sort
6. Merge Sort
7. Heap Sort
8. Quick Sort

## Running the Program

To run the applet, run `cli.py`. This can be run from an IDE (such as Thonny or IDLE), or by typing "python3 cli.py" into the command line.


## Other Details

As you can see, there are other sorts. These can be accessed in the `sorting_algorithms.py` file.

These are stored as a list of tuples that contain the function name and actual name in `app.py`, like this:

`IMPLEMENTED_SORTS = [("Python sorted()", "sorted_sort"),
                    ("List.sort()", "list_sort"),
                    ("Insertion Sort", "insertion_sort"),
                    ("Selection Sort", "selection_sort"),
                    ("Selection Sort v2", "selection_sort_v2"),
                    ("Bubble Sort", "bubble_sort"),
                    ("Merge Sort", "merge_sort"),
                    ("Heap Sort", "heap_sort"),
                    ("Heap Sort v2", "heap_sort_v2"),
                    ("Quick Sort", "quick_sort"),
                    ("Quick Sort v2", "quick_sort_v2")]`

Shell sort and other implementations of selection sort, quick sort, and heap sort can be found. They're definitely faster because sorts that I test are not optimized. I usually found some kind of pseudocode online, and then mimicked it to the best of my ability.

/wiki and /graph contains all of the wiki and graph files, which can be accessed from the applet itself. /icon includes an icon used in the applet.

`algorithm_tester.py` is a utility class that uses the timeit module. wiki_formatter is a utility class that extends tkinter.Text. wiki_formatting_rules.py contains data about how the wiki text files should be formatted.

If anyone ever reads this and has suggestions, please feel free to email me at dawsonren@gmail.com. I'd appreciate it.