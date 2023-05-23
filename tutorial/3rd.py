import numpy

a = numpy.array([1, 2, 3])
b = numpy.array([4, 5, 6])

c = [
    [1, 2],
    [3, 4]]
d = [
    [5, 6],
    [7, 8]]

print(a + b)
print(numpy.add(a, b))

print(a - b)
print(numpy.subtract(a, b))

print(a * b)
print(numpy.multiply(a, b))

print(a / b)
print(numpy.divide(a, b))

print(numpy.array(c) @ numpy.array(d))
print(numpy.dot(numpy.array(c), numpy.array(d)))
