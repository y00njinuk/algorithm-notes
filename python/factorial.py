'''
팩토리얼(Factorial)
- n! = 1 x 2 x 3 x .... x (n-1) x n
- 수학적으로 0!과 1!의 값은 1입니다.
'''

def factorial_iterataive(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iterataive(5))
print('재귀적으로 구현:', factorial_recursive(5))