def average(array):
    return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    print(average(list(map(int, input("Enter the array: ").split(" ")))))
