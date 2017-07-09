import numpy
if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    arr = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
    print(numpy.transpose(arr))
    print(arr.flatten())
