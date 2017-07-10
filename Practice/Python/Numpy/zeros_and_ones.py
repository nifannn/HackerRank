import numpy
if __name__ == '__main__':
    shap = [int(i) for i in input().split()]
    print(numpy.zeros(shap, dtype=numpy.int))
    print(numpy.ones(shap, dtype=numpy.int))
