from collections import deque
if __name__ == '__main__':
    for _ in range(int(input())):
        num = int(input())
        cubes = deque([int(c) for c in input().split()])
        flag = 'Yes'
        sorted_cubes = sorted(cubes, reverse=True)
        for c in sorted_cubes:
            if c == cubes[0]:
                cubes.popleft()
            elif c == cubes[-1]:
                cubes.pop()
            else: 
                flag = 'No'
                break
        print(flag)
