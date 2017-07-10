import numpy
if __name__ == '__main__':
    n ,m = [int(i) for i in input().split()]
    arr = [[int(i) for i in input().split()] for _ in range(n)]
    print(numpy.max(numpy.min(arr, axis=1)))
