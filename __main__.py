from .test_1 import Calculator

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(Calculator().sum(a, b))
