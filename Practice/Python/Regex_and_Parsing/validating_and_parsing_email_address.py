import re
import email.utils

if __name__ == '__main__':
    for _ in range(int(input())):
        name, addr = email.utils.parseaddr(input())
        if re.match(r'^[a-zA-Z][0-9a-zA-Z_.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', addr):
            print(email.utils.formataddr((name, addr)))
