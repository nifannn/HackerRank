import numpy
n = int(input())
mat_a = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
mat_b = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
print(numpy.dot(mat_a, mat_b))
