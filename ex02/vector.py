class Vector:

    def __init__(self, arg):
        self.values = []
        if type(arg) == list:
            for elem in arg:
                assert type(elem) == float
            self.values = arg
            self.size = len(self.values)
        elif type(arg) == tuple:
            assert len(arg) == 2
            try:
                int_vector = range(int(arg[0]), int(arg[1]))
                for val in int_vector:
                    self.values.append(float(val))
                self.size = int(arg[1]) - int(arg[0])
            except ValueError:
                print("Tuple of range not in good format")
                return
        elif type(arg) == int:
            assert arg >= 0
            int_vector = range(0, arg)
            for val in int_vector:
                self.values.append(float(val))
            self.size = arg
        else:
            print('Initialize vector with list<float> or int or range')

    def __add__(self, other):
        if type(other) is not Vector:
            print('Can only add two Vector types')
            return
        if self.size != other.size:
            print('Vectors are not the same dimension')
            return
        result_vec = []
        for s, o in zip(self.values, other.values):
            result_vec.append(s + o)
        return Vector(result_vec)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) is not Vector:
            print('Can only sub two Vector types')
            return
        if self.size != other.size:
            print('Vectors are not the same dimension')
            return
        result_vec = []
        for s, o in zip(self.values, other.values):
            result_vec.append(s - o)
        return Vector(result_vec)

    def __rsub__(self, other):
        if type(other) is not Vector:
            print('Can only sub two Vector types')
            return
        if self.size != other.size:
            print('Vectors are not the same dimension')
            return
        result_vec = []
        for s, o in zip(self.values, other.values):
            result_vec.append(o - s)
        return Vector(result_vec)

    def __truediv__(self, other):
        if type(other) is not int:
            print('Division allowed only between vector and scalar')
            return
        result_vec = []
        try:
            for val in self.values:
                result_vec.append(val / other)
        except ZeroDivisionError:
            print('Error: division by zero')
            return
        return Vector(result_vec)

    def __rtruediv__(self, other):
        print('Error: cannot divide by a scalar')

    def __mul__(self, other):
        if (type(other) != int and type(other) != Vector) or\
           (type(other) != int and self.size != other.size):
            print('Error: Multiplication allowed only between vector and',
                  ' scalar or two vectors of same dimension')
            return
        if type(other) == int:
            result_vec = []
            for val in self.values:
                result_vec.append(val * other)
            return Vector(result_vec)
        else:
            result = 0
            for s, o in zip(self.values, other.values):
                result += s * o
        return result

    def __rmul__(self, other):
        if type(other) is not int:
            print('Error: Multiplication allowed only between vector',
                  ' and scalar or two vectors of same dimension')
            return
        return self * other

    def __str__(self):
        if self.size == 0:
            print('<empty object Vector at address %x>' % hex(id(self)))
        str_format = '['
        for val in self.values:
            str_format += "{:.2f}, "
        str_format = str_format[:len(str_format) - 2] + ']'
        return(str_format.format(*(tuple(self.values))))

    def __repr__(self):
        return ('<object Vector at address %x>' % hex(id(self)))
