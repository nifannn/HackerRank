def merge_the_tools(string, k):
    while string:
        if len(string) > k:
            sub_string = string[:k]
            string = string[k:]
        else:
            sub_string = string[:]
            string = ''
        s = []
        for c in sub_string:
            if c not in s:
                s.append(c)
        print(''.join(s))

if __name__ == '__main__':
    merge_the_tools(input("Enter a string; "), int(input("Enter an integer: ")))
