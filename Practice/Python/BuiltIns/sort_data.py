if __name__ == '__main__':
    n, m = [int(c) for c in input().split()]
    numbers = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    for arr in sorted(numbers, key=lambda x: x[k]):
        print(*arr)
