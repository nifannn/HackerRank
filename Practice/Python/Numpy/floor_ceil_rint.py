import numpy
if __name__ == '__main__':
    arr = [float(i) for i in input().split()]
    for f in [numpy.floor, numpy.ceil, numpy.rint]:
        print(f(arr))
