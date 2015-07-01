''' matrix.py:
        Simple implementation of matrices. '''

class Matrix():
    def __init__(self, size, dimension):
        if hasattr(size, '__iter__'): 
            if len(size) != dimension:
                raise IndexError("Size array does not match the dimensions specified.")
            self.body = self.create_nonsquare_matrix(size, dimension)
        else:
            self.body = self.create_square_matrix(size, dimension)


    def create_square_matrix(self, size, n):
        """ Creates an n-dimension matrix with subarrays of size "size". """
        if n == 0: 
            return [0 for x in range(size)]
        else:
            return [self.create_square_matrix(size, n-1) for x in range(size)]

    def create_nonsquare_matrix(self, size_arr, n):
        """ Creates an n-dimension matrix where subarray k has size size_arr[k]. """
        if n == 1:
            return [0 for x in range(size_arr[n-1])]
        else:
            return [self.create_nonsquare_matrix(size_arr, n-1) for x in range(size_arr[n-1])]

    def flatten(self, target=self.body):
        return_array = []
        for x in target:
            if hasattr(x, 'flatten') or hasattr(x, '__iter__'):
                return_array = return_array +  self.flatten(x)
            else: return_array.append(x)
        return return_array

class TwoD_Matrix():
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.body = [[None for x in range(cols)] for y in range(rows)]

    def create_from_rows(self, row_array):
        marker = len(row_array[0])
        self.body = [x for x in row_array]

    def create_from_columns(self, column_array):
        marker = len(column_array[0])
        self.body = [x[j] for x, j in enumerate(column_array)]
