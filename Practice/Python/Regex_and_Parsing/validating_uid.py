import re
if __name__ == '__main__':
    for _ in range(int(input())):
        s = input()
        print('Valid' if not re.search(r'(.).*\1', s) and all([re.search(p, s) for p in [r'^[0-9a-zA-Z]{10}$', r'([A-Z].*){2}', r'([0-9].*){3}']]) else 'Invalid')
