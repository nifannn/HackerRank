def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number+1):
        s = ' '.join(['{:{width}{fmat}}'.format(i, width=width, fmat=f) for f in ['d', 'o', 'X', 'b']])
        print(s)

if __name__ == '__main__':
    print_formatted(int(input("Enter an integer: ")))
