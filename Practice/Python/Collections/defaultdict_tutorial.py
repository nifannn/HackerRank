from collections import defaultdict

if __name__ == '__main__':
    n, m = list(map(int, input().split(" ")))
    group_a = defaultdict(list)
    for idx in range(1, n+1):
        group_a[input()].append(idx)
    for _ in range(m):
        print(*(group_a.get(input(), [-1])))
