from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    s = ''.join(input().split(" "))
    k = int(input())
    ck = [1 if 'a' in comb else 0 for comb in combinations(s, k)]
    print("{:.3f}".format(sum(ck)/len(ck)))
