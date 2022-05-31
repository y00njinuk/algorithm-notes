'''
문제 예시 :
- 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요. 단 +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
- 예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 다음과 같습니다.
-> ((((0+2)x9)x8)x4) = 576 
'''

# 내가 생각한 풀이 
'''
1. 문자열 입력 받아서 리스트로 만든다.
2. 리스트의 순서대로 값을 가지고 오는데 0이 아니면 모두 곱한다.
'''
import sys
num_list = sys.stdin.readline().rstrip()
print(list(num_list))

result = int(num_list[0])
for index, num in enumerate(num_list[1:]):
    target = int(num)
    if target <= 1 or int(num_list[index]) <= 1:
        result += target
    else:
        result *= target

print(result)

'''
해결방법:
1. 두 수 중에서 하나라도 1 이하인 수가 나오면 더한다.
2. 그렇지 않으면 서로 곱한다.
'''
data = input()
# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)