def main(array, v):
    i = 0
    while i < len(array) and array[i] != v:
        i = i+1
    if i >= len(array):
        return None
    else:
        return i
