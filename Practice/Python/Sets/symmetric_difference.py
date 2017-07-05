if __name__ == '__main__':
    m = input("Enter integer M: ")
    set_a = set(map(int, input("Enter {} space-separated integers: ".format(m)).split(" ")))
    n = input("Enter integer N: ")
    set_b = set(map(int, input("Enter {} space-separated integers: ".format(n)).split(" ")))
    result = list((set_a.difference(set_b)) | (set_b.difference(set_a)))
    result.sort()
    for e in result:
        print(e)
