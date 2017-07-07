from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, n = input().split(" ")
    for sub in combinations_with_replacement(sorted(s), int(n)):
        print(''.join(sub))
