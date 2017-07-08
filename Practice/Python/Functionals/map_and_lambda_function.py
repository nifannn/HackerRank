cube = lambda x: x**3

def fibonacci(n):
    lst = [0,1]
    if n <= 2:
        return lst[:n]
    for i in range(2, n):
        lst.append(lst[-1] + lst[-2])
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
