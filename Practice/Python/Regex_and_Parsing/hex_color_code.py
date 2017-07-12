import re
if __name__ == '__main__':
    s = re.findall("[^\n](#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})", ".\n".join([input() for _ in range(int(input()))]))
    print(*s, sep='\n')
