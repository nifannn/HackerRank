import re
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        print('Valid' if re.search(r"^[456]([0-9]{15}|[0-9]{3}(-[0-9]{4}){3})$", s) and not re.search(r"([0-9])\1\1\1", s.replace("-", "")) else 'Invalid')
