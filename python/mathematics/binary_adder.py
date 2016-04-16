""" binary_adder.py: Takes two arrays representing binary numbers,
                     adds them together. """

__author__ = "David Vaillant"
__credits__ = "CLRS, Chapter 2.1"

def binary_add(x, y):
    """ Adds two "binary" arrays together. """
    assert(len(x) == len(y))

    z = [0] * (len(x)+1)
    for a, (i, j) in enumerate(zip(x[::-1], y[::-1])):
        if i and j:
            z[a] += 0
            z[a+1] += 1
        elif i or j:
            z[a] += 1
        else: pass

        if z[a] == 2:
            z[a+1] += 1
            z[a] -= 2
        
    return z[::-1]


