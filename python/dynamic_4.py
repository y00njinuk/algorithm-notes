'''
문제(효율적인 화폐 구성)
- N가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 합니다. 이 때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
- 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수입니다.
- M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.
'''

'''내가 푼거'''
# n, m = map(int, input().split())
# coins = list(map(int, input().split()))
# INF = 10001

# array = [INF] * (m+1)
# for coin in coins: array[coin] = 1
# for i in range(1, m+1):
#     for coin in coins:
#         if i % coin == 0 : 
#             array[i]= min(array[coin]*(i//coin), array[i]) 

# if array[m] == INF:
#     print(-1)
# else:
#     print(array[m])

'''
해결방법:
점화식 구성하기
ai = min(ai, ai-k+1)
'''

'''정답'''
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])