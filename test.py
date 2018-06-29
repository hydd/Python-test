import numpy
import matplotlib.pyplot as plt
x = numpy.arange(0, 5, 0.1)
print(x)
y = numpy.sinh(x)

plt.plot(x, y)
plt.show()