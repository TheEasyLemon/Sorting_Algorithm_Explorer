import random
import timeit
from .sorting_algorithms import *

def generate_set(l):
    """(int) ==> [list of int]
    Returns a contiguous list of unique integers above 0.
    """
    return random.shuffle([i + 1 for i in range(l)])

def generate_set_2(l):
    """(int) ==> [list of int]
    Returns a completely random list of unique integers above 0 and below 2*l.
    """
    return random.sample(range(1, 2 * l), l)

# TODO: remove generate_set(num) time because it shouldn't be counted
# as part of the time

class Algorithm_Tester(object):
    
    def __init__(self, name, func_name):
        """ (str, str) => (float)
        Takes the name of the sort and the function name, not the actual
        function itself. Returns the time taken to run 
        """
        self.name = name
        self.func_name = func_name

    def run(self, num = 100, repeat = 20):
        """ (int, int) => (float)
        Tests the sorting algorithm's ability to sort
        a list of length num. Does this repeat number of times.
        """
        
        # globals() contains sorting algorithms, which is not
        # imported in tester.py
        time_taken = timeit.timeit(f"{self.func_name}(generate_set_2({num}))",
                                   number = repeat, globals = globals())

        return time_taken

    def _max_test(self):
        """() => (tuple of [list of int], [list of int])
        Returns the data necessary to build a time complexity graph."""

        x = []
        y = []
        
        list_len = 10
        
        while True:
            time_taken = self.run(num=list_len, repeat=20)
            
            x.append(list_len)
            y.append(time_taken)

            
            # making sure the programs don't take too long to run
            if time_taken > 1:
                break
            elif time_taken > 0.1:
                list_len = round(list_len * 1.1)
            elif time_taken > 0.01:
                list_len = round(list_len * 3.5)
            else:
                list_len *= 10

        return x, y

    def _comp_test(self, test_values=[i * 20 for i in range(1, 51)]):
        """() => (tuple of [list of int], [list of int])
        Returns the data necessary to build a time complexity graph.
        However, it requires a list of test values to compare.
        Default list of test values is every 20 between 1 and 1000."""

        x = []
        y = []

        for list_len in test_values:
            time_taken = self.run(num=list_len, repeat=20)

            x.append(list_len)
            y.append(time_taken)

        return x, y

    def _write_values(self, mode = 0):
        # mode = 0 means max_values, mode = not 0 means comp_values
        if mode == 0:
            x, y = self._max_test()
            folder = "max_values"
        else:
            # do values between 
            x, y = self._comp_test()
            folder = "comp_values"

        with open(f"Sorting_Algorithm/graph/{folder}/{self.name}.txt", "w+") as file:
            # first line x values, second line y values
            file.write(",".join([str(v) for v in x]))
            file.write("\n")
            file.write(",".join([str(v) for v in y]))

    def get_values(self, mode = 0):
        # mode = 0 means max_values, mode = not 0 means comp_values
        if mode == 0:
            folder = "max_values"
        else:
            folder = "comp_values"
        
        with open(f"Sorting_Algorithm/graph/{folder}/{self.name}.txt", "r") as file:
            # first line x values, second line y values
            x = [float(v) for v in file.readline().strip().split(",")]
            y = [float(v) for v in file.readline().strip().split(",")]

        return x, y
