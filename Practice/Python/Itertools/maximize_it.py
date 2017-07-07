from itertools import product

if __name__ == '__main__':
    k, m = [int(i) for i in input().split(" ")]
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().split(" ")[1:])))
    print(max([sum(map(lambda x: x*x, comb))%m for comb in product(*arr)]))
