import numpy
if __name__ == '__main__':
    arr_a = numpy.array([int(i) for i in input().split(" ")])
    arr_b = numpy.array([int(i) for i in input().split(" ")])
    print(numpy.inner(arr_a, arr_b))
    print(numpy.outer(arr_a, arr_b))


