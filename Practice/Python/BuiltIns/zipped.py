if __name__ == '__main__':
    n, x = list(map(int, input().split()))
    scores = []
    for _ in range(x):
        scores.append(list(map(float, input().split())))
    for student in zip(*scores):
        print(sum(student)/len(student))
