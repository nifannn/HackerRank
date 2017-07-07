from collections import OrderedDict
if __name__ == '__main__':
    words = OrderedDict()
    for _ in range(int(input())):
        word = input()
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1
    print(len(words))
    print(*words.values())
