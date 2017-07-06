n = int(input())
s = set(map(int, input().split())) 
for _ in range(int(input())):
    cmd = input().split(" ")
    if cmd[0] == 'pop':
        cmd = "s.{}()".format(cmd[0])
    else:
        cmd = 's.{}({})'.format(*cmd)
    eval(cmd)
    
print(sum(s))
