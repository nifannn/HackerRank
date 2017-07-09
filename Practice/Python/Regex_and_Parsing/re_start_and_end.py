import re
if __name__ == '__main__':
    s = input()
    k = input()
    p = re.compile(k)
    m = p.search(s)
    if not m:
        print("(-1, -1)")
    while m:
        print("({}, {})".format(m.start(), m.end()-1))
        m = p.search(s, m.start() + 1)
