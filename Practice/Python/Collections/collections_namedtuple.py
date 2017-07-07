from collections import namedtuple
num = int(input())
Student = namedtuple('Student', input())
print('{:.2f}'.format(sum([int(Student(*(input().split())).MARKS) for _ in range(num)])/num))
