if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
       
    _, scores = zip(*students)
    second_lowest = min(set(scores) - {min(set(scores))})
    result = [name for name, score in students if score == second_lowest]           result.sort()
    for name in result:
        print(name)
