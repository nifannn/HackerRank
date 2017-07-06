if __name__ == '__main__':
    n = int(input())
    rooms = list(map(int, input().split(" ")))
    rooms_set = set(rooms)
    print((sum(rooms_set)*n - sum(rooms))//(n-1))
