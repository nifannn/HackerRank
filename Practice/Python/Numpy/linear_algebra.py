import numpy
arr = numpy.array([[float(i) for i in input().split()] for _ in range(int(input()))])
print(numpy.linalg.det(arr))
