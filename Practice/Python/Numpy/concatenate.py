import numpy
if __name__ == '__main__':
    n, m, p = [int(i) for i in input().split()]
    arr_a = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
    arr_b = numpy.array([[int(i) for i in input().split()] for _ in range(m)])
    print(numpy.concatenate((arr_a, arr_b), axis=0))
