from functools import partial

# utility functions
def repeatinput(message, func = lambda a : a):
    """(str, list of str) => type(func)

    Repeats "Please enter a valid value." until the user's input
    is a legitimate entry through func.

    Enter "quit" to escape.

    """

    while True:
        user_input = input(message)
        # check exit condition
        if user_input == "quit":
            return
        try:
            formatted_input = func(user_input)
            break
        except ValueError:
            print("Not a valid input.")

    return formatted_input

intinput = partial(repeatinput, func = int)
floatinput = partial(repeatinput, func = float)
