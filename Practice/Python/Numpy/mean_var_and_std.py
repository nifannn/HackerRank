import numpy
if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    arr = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
    print(numpy.mean(arr, axis=1))
    print(numpy.var(arr, axis=0))
    print(numpy.std(arr, axis=None))
