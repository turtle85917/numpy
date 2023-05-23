import numpy

a = [
    [1, 2, 3],
    [4, 5, 6]]
b = numpy.array(a)
print(b)
print(b.ndim)
print(b.shape)
print(b[0, 0])

print(numpy.arange(10))
print(numpy.arange(5, 10))

print(numpy.zeros((2, 2)))
print(numpy.zeros(b.shape))

print(numpy.ones((2, 3)))

print(numpy.full((2, 3), 5))

print(numpy.eye(3))
