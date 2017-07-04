if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max_item = max(arr)
    while max_item in arr:
        arr.remove(max_item)
    print(max(arr))
    
