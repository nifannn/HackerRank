def print_rangoli(size):
    final_e = ord('a') + size - 1
    width = 4 * size - 3
    for i in range(size):
        s = list(range(final_e, final_e-i, -1)) + [final_e-i] + list(range(final_e-i+1, final_e+1))
        s = ('-'.join([chr(e) for e in s])).center(width,'-')
        print(s)
        
    for i in range(size-2,-1,-1):
        s = list(range(final_e, final_e-i, -1)) + [final_e-i] + list(range(final_e-i+1, final_e+1))
        s = ('-'.join([chr(e) for e in s])).center(width,'-')
        print(s)

if __name__ == '__main__':
    print_rangoli(int(input('Enter the size: ')))
