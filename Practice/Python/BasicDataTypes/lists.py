if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        s = input().split(" ")
        cmd = s[0]
        args = s[1:]
        
        if cmd == 'print':
            print(arr)
        else:
            cmd = 'arr.' + cmd + '(' + ','.join(args) + ')'
            eval(cmd)
