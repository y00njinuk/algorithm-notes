'''
문제(금광)
- n x m 크기의 금광이 있습니다. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
- 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 잇습니다. 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.
'''
'''
해결방법:
점화식 구성
dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
-> 채굴량의최대값 = 현재채굴량 + max(오른쪽위에서온최대채굴량, 오른쪽에서온최대채굴량, 오른쪽아래에서온최대채굴량)
'''


'''정답'''
# 테스트케이스 개수 입력받고 해당 개수 만큼 반복
for tc in range(int(input())):
    n, m = map(int, input.split())
    # 2차원 배열의 원소를 한 줄로 입력받기
    array = list(map(int, input().split))

    dp = []
    index = 0
    # m개 만큼 리스트로 만들어서 dp 배열에 추가
    for i in range(n): # n 크기의 행이 생성될 때
        dp.append(array[index:index+m]) # m 크기의 열 만큼을 배열로 만들고 할당한다
        index += m 
    
    for j in range(1, m):
        for i in range(n):
            # 왼쪽위
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽아래
            if i == n-1: left_down=0
            else: left_down = dp[i+1][j-1]
            #왼쪽
            left = dp[i][j-1]
            #최대채굴량
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)