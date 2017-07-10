import numpy
if __name__ == '__main__':
    print(numpy.eye(*[int(i) for i in input().split()]))
