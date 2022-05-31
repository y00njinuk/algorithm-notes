'''
문제(병사배치하기)
: https://www.acmicpc.net/problem/18353
'''
# i명의 병사에서 남아있는 최대 병사의수 = 현재 병사의 수 - 열외할 병사의 최소의 수
# 열외할 병사의 최소의 수 = 열외 가능한 병사의 수 중 최소값
# 열외 가능한 병사 = 내림차순에 맞지 않는 전투력을 가진 병사
# 내림차순에 맞지 않는 전투력을 가진 병사 = 이전의 배치된 병사의 전투력보다 높은 수


'''내가 푼거(오답)'''
# n = int(input())
# array = list(map(int, input().split()))
# dp = [0] * n
# dp[0] = array[0]

# for i in range(1, n):
#     if dp[i] > dp[i-1]:
#         dp[i-1] = array[i]
#     else:
#         dp[i] = array[i]

# print(dp)

'''
해결방법
- 이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)로 알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같습니다.
- 예를 들어 하나의 수열 array={4,2,5,8,11,15}이 있다고 합시다.
    -> 이 수열의 가장 긴 증가하는 부분 수열은 {4,5,8,11,15}입니다.
- 본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치환할 수 있으므로, LIS 알고리즘을 조금 수정하여 적용함으로서 정답을 도출할 수 있습니다.

- D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
- 점화식은 다음과 같습니다.
모든 0≤j＜1에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
'''
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))