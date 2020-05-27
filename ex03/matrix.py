from vector import Vector


class Matrix:

    data = []
    shape = (0, 0)

    def __check_list_of_list(self, lst):
        try:
            first = True
            size = 0
            for el in lst:
                assert type(el) is list
                if first:
                    size = len(el)
                    first = False
                else:
                    assert len(el) == size
                for n in el:
                    try:
                        f = float(n)
                    except ValueError:
                        raise ValueError
        except AssertionError:
            raise AssertionError

    def __init__(self, *argv):
        if len(argv) == 1:
            arg = argv[0]
            if type(arg) is list:
                try:
                    self.__check_list_of_list(arg)
                except AssertionError:
                    print('Error: The data must be a list of',
                          'lists of same dimension')
                    return
                except ValueError:
                    print('Error: The data must be a list of',
                          'lists of floats')
                    return
                self.data = arg
                rows = len(arg)
                columns = len(arg[0])
                self.shape = (rows, columns)
            elif type(arg) is tuple:
                try:
                    assert len(arg) is 2
                    assert type(arg[0]) is int and type(arg[1]) is int
                except AssertionError:
                    print('Error: Shape tuple must be two integers')
                    return
                self.shape = arg
                self.data = [[0.] * arg[1]] * arg[0]
        elif len(argv) == 2:
            data = argv[0]
            shape = argv[1]
            if type(data) is list:
                try:
                    self.__check_list_of_list(data)
                except AssertionError:
                    print('Error: The data must be a list of',
                          'lists of same dimension')
                    return
                except ValueError:
                    print('Error: The data must be a list of',
                          'lists of floats')
                    return
            rows = len(data)
            columns = len(data[0])
            try:
                assert type(shape) is tuple and len(shape) == 2
                assert type(shape[0]) is int and type(shape[1]) is int
                assert rows == shape[0] and columns == shape[1]
            except AssertionError:
                print('Error: Shape does not correspond to data')
                return
            self.data = data
            self.shape = shape

    def __add__(self, other):
        if type(other) is not Matrix:
            print('Error: Can only add two matrices')
            return
        if other.shape != self.shape:
            print('Error: Matrices are not the same shape')
            return
        result_matrice = []
        for s, o in zip(self.values, other.values):
            new_vec = []
            for s_vec, o_vec in zip(s, o):
                new_vec.append(s_vec + o_vec)
            result_matrice.append(new_vec)
        return Matrix(result_matrice)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == Matrix:
            return self + (other * -1)
        else:
            print("Error: Can only substract two matrices")

    def __rsub__(self, other):
        if type(other) == Matrix:
            return (self * -1) + other
        else:
            print("Error: Can only substract two matrices")

    def __truediv__(self, other):
        if type(other) is int:
            try:
                result_matrice = []
                for vec in self.data:
                    new_vec = []
                    for s in vec:
                        new_vec.append(s / other)
                    result_matrice.append(new_vec)
                return Matrix(result_matrice)
            except ZeroDivisionError:
                print('Error: division by zero')
                return
        else:
            print('Error: Division allowed only between matrice and',
                  'scalar')

    def __rtruediv__(self, other):
        if type(other) != Matrix:
            print('Error: Cannot divide by Matrix')
            return
        return other / self

    def __mul__(self, other):
        if type(other) is Vector:
            if other.size != self.shape[0]:
                print('Error: multiplication only allowed by a',
                      'Vector of same dimension')
                return
            new_vec = []
            for n in range(0, self.shape[1]):
                sm = 0
                for i in range(0, other.size):
                    sm += other.values[i] * self.data[n][i]
                new_vec.append(sm)
            return Vector(new_vec)
        elif type(other) is Matrix and self.shape == tuple(
             reversed(other.shape)):
            result_matrice = []
            for i in range(0, self.shape[0]):
                new_vec = []
                for j in range(0, self.shape[1]):
                    sm = 0
                    for k in range(0, self.shape[0]):
                        sm += self.data[i][k] * other.data[k][j]
                    new_vec.append(sm)
                result_matrice.append(new_vec)
            return Matrix(result_matrice)
        elif type(other) is int:
            result_matrice = []
            for vec in self.data:
                new_vec = []
                for s in vec:
                    new_vec.append(s * other)
                result_matrice.append(new_vec)
            return Matrix(result_matrice)
        else:
            print('Error: Multiplication allowed only between matrice and',
                  ' scalar or two matrices of compatible shape')

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        str_format = '['
        for vec in self.data:
            str_format += '['
            for val in vec:
                str_format += "{:.1f}, "
            str_format = str_format[:len(str_format) - 2] + '], '
        str_format = str_format[:len(str_format) - 2] + ']'
        big_data = []
        for data in self.data:
            for val in data:
                big_data += [val]
        return(str_format.format(*(tuple(big_data))))

    def __repr__(self):
        return ('<object Vector at address %s>' % hex(id(self)))
