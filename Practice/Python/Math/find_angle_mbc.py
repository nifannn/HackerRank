import math
    
if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    print('{}°'.format(round(math.atan(ab/bc)*180/math.pi)))
