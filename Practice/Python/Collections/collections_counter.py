from collections import Counter

if __name__ == '__main__':
    x = int(input())
    shoes = Counter([int(size) for size in input().split(" ")])
    earned = 0
    for _ in range(int(input())):
        size, price = list(map(int, input().split(" ")))
        if shoes.get(size, 0):
            earned = earned + price
            shoes[size] = shoes[size] - 1
    print(earned)
