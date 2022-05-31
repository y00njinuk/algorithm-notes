'''
def 함수명(매개변수)
    실행할 소스코드
    return 반환값
'''
def add(a,b):
    return a+b

# print(add(3,7))
# print(add(b=3, a=11))

# global variable
a = 0

def func():
    global a # define global
    a += 7

func()
print(a)


# return value 
def operator(a, b):
    return a+b, a-b, a*b, a/b

a, b, c, d = operator(3,7)
print(a,b,c,d)