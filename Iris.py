from sklearn import datasets
import  math
def getData():
    iris = datasets.load_iris()
    return iris
def RSA(n):
    p = 3;q = 11
    n = p*q
    delphiN = (p-1)*(q-1)

if __name__ == '__main__':
    print(getData())