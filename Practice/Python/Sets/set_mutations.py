if __name__ == '__main__':
    n = input()
    set_a = set(map(int, input().split(" ")))
    for _ in range(int(input())):
        cmd = input().split(" ")[0]
        set_b = set(map(int, input().split(" ")))
        eval("set_a.{}(set_b)".format(cmd))
        
    print(sum(set_a))
