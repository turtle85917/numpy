import numpy
import matplotlib.pyplot as pyplot

x = numpy.random.uniform(size=100)
x.reshape(20, 5)

print(x)

pyplot.plot(x)
pyplot.show()
