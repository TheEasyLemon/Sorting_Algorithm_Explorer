"""
Sorting algorithms! Just with sets of integers so it's easier.
Descriptions of sorting algorithms and pseudocode implementations
(which I converted into Python) are courtesy of wikipedia.com.

Dawson Ren, 4/10/20
"""


from heapq import *  # used for heap_sort_v2
import math

# python sorted() function
def sorted_sort(li):
    """ (int, int) => ()
    Runs the python-given sorted() test. To my best knowledge, sorted()
    uses some kind of a merge sort.
    """
    return sorted(li)

# python list.sort() method
def list_sort(li):
    """ (int, int) => ()
    Runs the python list .sort() method. Uses a specialized merge sort
    called a "timsort" - named after a guy named Tim :)
    https://en.wikipedia.org/wiki/Timsort

    n is the length of the set tested.
    r is the how many times timeit repeats.
    """
    return li.sort()

def insertion_sort(li):
    """ [list of int] => [list of int]
    Insertion sort: works by taking elements from the list one
    by one and inserting them in their correct position into a
    new sorted list similar to how we put money in our wallet.
    """

    # append first item of li
    sorted_list = [li[0]]

    # for all other items in li
    for i in range(1, len(li)):
        current_item = li[i]

        # iterate through sorted_list to compare to current_item
        for j in range(len(sorted_list)):
            # if the current_item is less than the item in sorted_list
            # append to sorted_list
            if current_item < sorted_list[j]:
                sorted_list.insert(j, current_item)
                break
        else:
            # if current_item is larger than all the values in sorted_list
            sorted_list.append(current_item)

    return sorted_list

def selection_sort(li):
    """ [list of int] => [list of int]
    Selection sort: finds the minimum value, swaps it with the
    value in the first position, and repeats these steps for
    the remainder of the list.
    """

    sorted_list = li

    # iterate as many times as the list is long
    for i in range(len(sorted_list)):
        # initial minimum is just the first value of the unsorted list
        min_index = i

        # find the minimum in the unsorted list
        for j in range(i, len(sorted_list)):
            # if current is less than current min set new minimum
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j

        # swap the minimum and start of unsorted list
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list


def selection_sort_v2(li):
    """ [list of int] => [list of int]
    Same as selection_sort except it takes advantage of min() function.
    """
    sorted_list = li

    # iterate as many times as the list is long
    for i in range(len(sorted_list)):
        # find the minimum in the unsorted list
        minimum = min(sorted_list[i:])
        # locates the index of the minimum
        min_index = sorted_list.index(minimum)

        # swap the minimum and start of unsorted list
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list


def bubble_sort(li):
    """ [list of int] => [list of int]
    Bubble sort: starts at the beginning of the data set.
    It compares the first two elements, and if the first is
    greater than the second, it swaps them. It continues doing
    this for each pair of adjacent elements to the end of the
    data set. It then starts again with the first two elements,
    repeating until no swaps have occurred on the last pass.
    """
    # boolean to keep track of whether the algorithm is sorted
    unsorted = True

    while unsorted:
        # assume it's sorted
        unsorted = False
        for i in range(len(li) - 1):
            if li[i] > li[i + 1]:
                # it is unsorted
                unsorted = True
                # swap elements
                li[i], li[i + 1] = li[i + 1], li[i]

    return li


def merge_sort(li):
    """ [list of int] => [list of int]
    Merge sort: divides the unsorted list into n sublists, each
    containing one element (a list of one element is considered
    sorted). Repeatedly merges sublists to produce new sorted sublists
    until there is only one sublist remaining.

    Uses a top-down implementation using recursion.
    """

    # base case
    if len(li) <= 1:
        return li

    # recursive case
    left = []
    right = []
    # split into left and right
    for i in range(len(li)):
        if i < len(li) // 2:
            left.append(li[i])
        else:
            right.append(li[i])

    # sort the lists
    left = merge_sort(left)
    right = merge_sort(right)

    # merge the lists
    result = []

    # while left and right aren't empty
    while len(left) > 0 and len(right) > 0:
        # compare the first element of each list
        if left[0] <= right[0]:
            # append smaller value to result
            result.append(left[0])
            # remove the first value of left
            del left[0]
        else:
            # append smaller value to result
            result.append(right[0])
            # remove the first value of right
            del right[0]

    # it is possible there are still items in left or right (but not both!)
    result.extend(left)
    result.extend(right)

    return result


def heap_sort(li):
    """ [list of int] => [list of int]
    Heap sort: divides its input into a sorted and an unsorted region,
    and it iteratively shrinks the unsorted region by extracting the
    largest element from it and inserting it into the sorted region.
    It does not waste time with a linear-time scan of the unsorted region;
    rather, heap sort maintains the unsorted region in a heap data structure
    to more quickly find the largest element in each step.

    To implement a heap using arrays, we will use the rule
    li[k] >= li[2*k+1] and li[k] >= li[2*k+2] (left child and right child
    respectively).

    More generally, the array must satisfy the heap quality:
        For any given node C, if P is a parent node of C, then
        the value of P is greater than or equal to the key of C
        (for max heaps)
    
    Graphically, this would look like:
    
                                  0
                 1                                2

          3              4                5               6

      7       8       9       10      11      12      13      14

    15 16   17 18   19 20   21  22  23  24  25  26  27  28  29  30
    """

    def heapify(lst, heap_size, root):
        """ ([list of int], int, int) => [list of int]
        Rearranges the list to satisfy the heap quality.
        Root is index of the largest element in the lst.
        """
        # the largest node
        largest = root
        left_child = 2 * largest + 1
        right_child = 2 * largest + 2

        # check if left_child and root need to be swapped
        if left_child < heap_size and lst[largest] < lst[left_child]:
            largest = left_child

        # check if right_child and root need to be swapped
        if right_child < heap_size and lst[largest] < lst[right_child]:
            largest = right_child

        # change root, if needed
        if largest != root:
            lst[root], lst[largest] = lst[largest], lst[root]
            # continue to heapify the root
            heapify(lst, heap_size, largest)

    # Build a maxheap by iterating through the list backwards
    for i in range(len(li), -1, -1):
        heapify(li, len(li), i)

    print(li)

    # extract elements one by one
    for i in range(len(li) - 1, 0, -1):
        """remember, heap sort differs from insertion sort in that
        # it searches for the maximum, rather than minimum, element.
        li[0:end] is a heap (like a tree, but elements are not guaranteed
        to be sorted) and li[end:len(li)] is in sorted order."""
        li[i], li[0] = li[0], li[i]
        # return to heap, since the heap was messed up by swapping
        heapify(li, i, 0)

    return li


def heap_sort_v2(li):
    """ [list of int] => [list of int]
    Same as heap_sort except it takes advantage of the heapq library
    in the PST (python standard library).

    Important note: heapq uses a "min heap" interpretation, so the
    topmost element is the smallest, rather than largest.
    """

    h = []
    for i in li:
        # heapify the values of the list by putting it onto a heap
        heappush(h, i)

    # pop the smallest values off one by one for the entire heap
    return [heappop(h) for _ in range(len(h))]

def quick_sort(li):
    """([list of int], int, int) => [list of int]
    Quick sort: works by selecting a 'pivot' element from the array
    and partitioning the other elements into two sub-arrays, according
    to whether they are less than or greater than the pivot. The
    sub-arrays are then sorted recursively.

    This version will use the Lomuto partition scheme, where the pivot
    is the last element of the list in question.
    "l" (for low) is the first element of the list "li", and "h" is the
    last (for high).
    """
    
    def partition(lst, low, high):
        """ ([list of int], int, int) => int
        Partitions the list "lst" so that every element greater than an
        arbitrarily selected pivot (the element at index high) ends up
        on the right of the pivot index, and every element smaller ends
        up on the left.

        Note: high is excluded.
        """
        # pivot is last item of the bracket [low, high)
        pivot = lst[high - 1]
        # counter for index of item to swap
        i = low

        # iterate through low to high
        for j in range(low, high):
            if lst[j] < pivot:
                # swap if item needs to be swapped
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        # swap the pivot and the middle point (index i)
        lst[i], lst[high - 1] = lst[high - 1], lst[i]

        # return pivot index
        return i

    def sorter(li, l, h):
        """ ([list of int], int, int) => [list of int]
        Driver for the recursive sort function.
        """
        if l < h:
            p = partition(li, l, h)
            # sort the partition to the left
            sorter(li, l, p)
            # sort the partition to the right
            sorter(li, p + 1, h)

        return li

    return sorter(li, 0, len(li))

def quick_sort_v2(li):
    """([list of int], int, int) => [list of int]
    Quick sort: works by selecting a 'pivot' element from the array
    and partitioning the other elements into two sub-arrays, according
    to whether they are less than or greater than the pivot. The
    sub-arrays are then sorted recursively.

    This version will use the Hoare partition scheme, where the pivot
    is calculated in the middle instead of at the end of the list.
    "l" (for low) is the first element of the list "li", and "h" is the
    last (for high).
    """
    def partition(lst, low, high):
        """ ([list of int], int, int) => int
        Partitions the list "lst" so that every element greater than an
        arbitrarily selected pivot (the element at index high) ends up
        on the right of the pivot index, and every element smaller ends
        up on the left.

        Note: high is excluded.
        """
        # pivot is middle item of the bracket [low, high)
        pivot = lst[(high + low) // 2]
        # counter for index of item to swap
        i = low
        j = high - 1

        # the only exit condition is when i and j meet
        while True:
            # find a lst[i] out of place
            while lst[i] < pivot:
                i += 1
            # find a lst[j] out of place
            while lst[j] > pivot:
                j -= 1
            
            # go until i and j meet
            if i >= j:
                return j
            # swap the out of place elements
            lst[i], lst[j] = lst[j], lst[i]
    
    def sorter(li, l, h):
        """ ([list of int], int, int) => [list of int]
        Driver for the recursive sort function.
        """
        if l < h:
            p = partition(li, l, h)
            # sort the partition to the left
            sorter(li, l, p)
            # sort the partition to the right
            sorter(li, p + 1, h)

        return li

    return sorter(li, 0, len(li))

##### DEV NOTE: DOESN'T WORK #####

def shell_sort(li):
    """ [list of int] => [list of int]
    Shell sort: arranges the list of elements so that,
    starting anywhere, considering every hth element
    gives a sorted list. Such a list is said to be h-sorted.
    
    Beginning with large values of h, this rearrangement allows
    elements to move long distances in the original list,
    reducing large amounts of disorder quickly, and leaving
    less work for smaller h-sort steps to do.

    Determining which values of h we should use is a continuing problem
    in computer science. I'll be using the simple sequence of powers of two,
    which seem to work best for me.

    See https://en.wikipedia.org/wiki/Shellsort for more information.
    """
    
    # calculating values of h (gaps), 1 is always the last gap (obviously)
    gaps = []
    k = 1
    while 2 ** k < len(li):
        gaps.append(2 ** k)
        k += 1
    
    # sorting by gaps, starting with the largest (last) gap
    for gap in reversed(gaps):
        
        # iterate through unsorted values as li[0:gap-1] is considered sorted
        # by virtue of being the only value in our sorted list
        for i in range(gap, len(li)):
            # select value to be inserted
            value = li[i]
            
            # new counter variable that can be changed, so i
            # variable stays unchanged
            j = i

            # check value against the element h spaces before
            # if the element h spaces before is larger, we need to swap
            while j >= gap and li[j - gap] >= value:
                li[j] = li[j - gap]
                # go back gap spaces to check value against element h
                # space before, in case another swap is needed
                j -= gap

            # replace the original value
            li[j] = value
    
    return li


# Short driver code just to make sure they're actually sorting stuff:

def main():
    seq = [2,3,7,5,11,8,15,4,9,6]
    print(heap_sort(seq))


if __name__ == "__main__":
    main()


