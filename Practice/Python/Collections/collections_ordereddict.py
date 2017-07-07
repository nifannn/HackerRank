from collections import OrderedDict

if __name__ == '__main__':
    items = OrderedDict()
    for _ in range(int(input())):
        s = input().split()
        price = int(s[-1])
        name = " ".join(s[0:-1])
        if name not in items:
            items[name] = price
        else:
            items[name] = items[name] + price
    for name, net in items.items():
        print(name, net)
