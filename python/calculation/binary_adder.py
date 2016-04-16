""" binary_adder.py: Takes two arrays representing binary numbers,
                     adds them together. """

__author__ = "David Vaillant"
__credits__ = "CLRS, Chapter 2.1"

def binary_add(x, y):
    """ Adds two binary arrays together. """
    # Makes sure that the arrays have the same length.
    # Could be changed to padding on extra zeroes, if so desired.
    assert(len(x) == len(y))

    z = [0] * (len(x)+1)
    for a, (i, j) in enumerate(zip(x[::-1], y[::-1])):
        # Makes sure that the array is a binary array.
        # Strictly speaking, not necessary. But nice.
        if i not in [0, 1]: return False
        if j not in [0, 1]: return False

        # if i and j are both 1 
        if i and j:
            z[a] += 0
            z[a+1] += 1
        # if only one of them is 1
        elif i or j:
            z[a] += 1
        # if they're both 0
        else: pass

        if z[a] == 2:
            z[a+1] += 1
            z[a] -= 2
        
    return z[::-1]

def unit_test():
    """ Unit tests. """
    x_arr = ( [1, 0, 0],
              [1],
              [0],
              [1, 0, 0, 1],
              [1, 1, 1, 1],
              [1, 0, 0, 0, 0])
    y_arr = ( [0, 1, 1],
              [0],
              [0, 0],
              [1, 1, 0, 0],
              [0, 0, 0, 0],
              [1, 0, 0, 0, 0])
    z_arr = ( [0, 1, 1, 1],
              [0, 1],
              None,
              [1, 0, 1, 0, 1],
              [0, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0] )
    for a, (x, y) in enumerate(zip(x_arr, y_arr)):
        sum = binary_add(x, y)
        print("Adding {} to {}.".format(x, y))
        if sum == z_arr[a]:
            print("Successfully returned {}.".format(sum))
        else:
            print("Got {} instead of {}.".format(sum, z_arr[a]))
        print()

if __name__ == "__main__":
    unit_test()
