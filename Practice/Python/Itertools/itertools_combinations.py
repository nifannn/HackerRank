from itertools import combinations

if __name__ == '__main__':
    s, n = input().split(" ")
    for i in range(1, int(n)+1):
        for sub in combinations(sorted(s), i):
            print(''.join(sub))
