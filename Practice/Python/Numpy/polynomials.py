import numpy
if __name__ == '__main__':
    coe = [float(i) for i in input().split(" ")]
    x = float(input())
    print(numpy.polyval(coe, x))
