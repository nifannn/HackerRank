def wrapper(f):
    def fun(l):
        s = [" ".join(["+91", number[-10:-5], number[-5:]]) for number in l]
        return f(s)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


