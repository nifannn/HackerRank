import re
if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        try:
            float(n)
            print(bool(re.search(r"^[+-.0-9]?.[0-9]+", n)))
        except:
            print('False')
