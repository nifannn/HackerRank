import numpy
if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    arr_a = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
    arr_b = numpy.array([[int(i) for i in input().split()] for _ in range(n)])
    print(arr_a + arr_b)
    print(arr_a - arr_b)
    print(arr_a * arr_b)
    print(arr_a // arr_b)
    print(arr_a % arr_b)
    print(arr_a ** arr_b)
