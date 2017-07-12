import re
if __name__ == '__main__':
    for _ in range(int(input())):
        print(re.sub(r"(?<= )(&|\|)\1 ", lambda x: 'and ' if x.group() == '&& ' else 'or ', input()))
