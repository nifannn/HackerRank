import re

if __name__ == '__main__':
    for _ in range(int(input())):
        print('YES' if re.match(r'^[789][0-9]{9}$', input()) else 'NO')
