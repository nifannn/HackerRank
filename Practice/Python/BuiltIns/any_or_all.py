n = int(input())
arr = input().split()
print(all([int(num) > 0 for num in arr]) and any([num[::-1] == num for num in arr]))
