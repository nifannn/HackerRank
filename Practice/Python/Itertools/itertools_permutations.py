from itertools import permutations

if __name__ == '__main__':
    s, n = input().split(" ")
    for sub in permutations(sorted(s), int(n)):
        print(''.join(sub))
