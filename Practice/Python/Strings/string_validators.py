if __name__ == '__main__':
    s = input()
    is_list = list(zip(*[[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s]))
    print_list = [True if True in is_result else False for is_result in is_list]
    for result in print_list:
        print(result)
