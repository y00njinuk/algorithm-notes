'''
재귀 함수(Recursive Function)이란 자기 자신을 다시 호출하는 함수를 의미합니다.
- 단순한 형태의 재귀 함수 예제
-> '재귀 함수를 호출합니다'라는 문자열을 무한히 출력합니다.
-> 어느정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력됩니다.
'''

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

# recursive_function()

'''
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료조건을 반드시 명시한다.
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있습니다.
'''

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)