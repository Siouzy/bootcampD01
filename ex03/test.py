from matrix import Matrix
from vector import Vector

m1 = Matrix((4, 2))
print(m1)
print(m1.data)
m2 = Matrix([[0.1, 0.2, 0.3], [1.1, 1.2, 1.3], [2.3, 3.7, 9.7]])
print(m2)
print(m2.data)
m3 = Matrix([[5.1, 5.2, 0.3], [7.1, 1.2, 1.3], [2.3, 3.7, 9.7]], (3, 3))
print(m3)
print(m3.data)

print(m3 * 4)
print(m3 * Vector([1., 2., 3., 4.]))
print(m3 * Vector([1., 2., 3.]))
print(m3 * m1)

m4 = Matrix((3, 3))
print(m3 / m4)
print(m3 * m4)
print(m3 / m2)
print(m3 * m2)
print(3 / m2)
print(3 * m2)