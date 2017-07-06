if __name__ == '__main__':
    countries = set()
    for _ in range(int(input("Enter number of countries: "))):
        countries.add(input("Enter one country: "))
    print("Number of distinct countries: {}".format(len(countries)))
