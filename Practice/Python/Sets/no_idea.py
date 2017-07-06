if __name__ == '__main__':
    n, m = list(map(int, input().split(" ")))
    arr = list(map(int, input().split(" ")))
    set_a = set(map(int, input().split(" ")))
    set_b = set(map(int, input().split(' ')))
    print(sum([1 if e in set_a else -1 if e in set_b else 0 for e in arr]))
