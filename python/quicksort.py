def main(arr):
    remain(arr, 0, len(arr))

def remain(arr, p, r):
    if p<r:
        q = partition(arr, p, r)
        remain(arr, p, q-1)
        remain(arr, q+1, r)


