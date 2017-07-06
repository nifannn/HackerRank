set_a = set(map(int, input().split(" ")))
result = []
for _ in range(int(input())):
    set_b = set(map(int, input().split(" ")))
    result.append((set_a | set_b) == set_a and set_a != set_b)
print(False not in result)
