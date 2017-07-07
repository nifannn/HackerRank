from itertools import groupby

if __name__ == '__main__':
    s = input()
    print(' '.join(map(str, [(len(list(g)),int(k)) for k, g in groupby(s)])))
