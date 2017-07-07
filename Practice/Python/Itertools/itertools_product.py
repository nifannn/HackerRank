from itertools import product

if __name__ == '__main__':
    lst_a = list(map(int, input().split(" ")))
    lst_b = list(map(int, input().split(" ")))
    print(" ".join(map(str, list(product(lst_a, lst_b)))))
