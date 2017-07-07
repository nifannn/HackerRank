from collections import deque
if __name__ == '__main__':
    q = deque()
    for _ in range(int(input())):
        cmd = input().split()
        if len(cmd) > 1:
            eval('q.{}({})'.format(*cmd))
        else:
            eval('q.{}()'.format(*cmd))
    print(*q)
