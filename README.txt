Welcome to Dawson’s Algorithm Explorer!

This is an interactive applet that compares, explains, and interactively displays sorting algorithms. The currently implemented algorithms are:
- Python sorted()
- List.sort()
- Insertion Sort
- Selection Sort
- Bubble Sort
- Merge Sort
- Heap Sort
- Quick Sort
These are stored as a list of tuples that contain the function name and actual name in app.py, like this:
IMPLEMENTED_SORTS = [("Python sorted()", "sorted_sort"),
                    ("List.sort()", "list_sort"),
                    ("Insertion Sort", "insertion_sort"),
                    ("Selection Sort", "selection_sort"),
                    ("Selection Sort v2", "selection_sort_v2"),
                    ("Bubble Sort", "bubble_sort"),
                    ("Merge Sort", "merge_sort"),
                    ("Heap Sort", "heap_sort"),
                    ("Heap Sort v2", "heap_sort_v2"),
                    ("Quick Sort", "quick_sort"),
                    ("Quick Sort v2", "quick_sort_v2")]

As you can see, there are other sorts. These can be accessed in the sorting_algorithms.py file. In tester.py, you can individually test all of them.

To run the applet, run cli.py. This can be run from an IDE (such as Thonny or IDLE), or by typing "python3 cli.py" into the command line.

/wiki and /graph contains all of the wiki and graph files, which can be accessed from the applet itself. /icon includes an icon used in the applet.

algorithm_tester.py is a utility class that uses the timeit module. wiki_formatter is a utility class that extends tkinter.Text. wiki_formatting_rules.py contains data about how the wiki text files should be formatted.

__pycache__ is the C++ code of this file, so the scripts can execute more quickly.

This software uses the MIT license, which can be found in LICENSE.txt.