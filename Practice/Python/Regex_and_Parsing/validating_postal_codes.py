import re
s = input()
print(all([re.search(r'^[1-9][0-9]{5}$', s), len(re.findall(r'([0-9])(?=.\1)', s)) <= 1]))
