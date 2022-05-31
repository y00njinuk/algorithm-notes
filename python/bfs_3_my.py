from collections import deque

def bfs(x, y, virus):
    # 처음 바이러스가 증식하는 좌표
    next_queue = deque()
    next_queue.append((x, y))
    now_queue = deque()

    # 1초가 지난 뒤 바이러스가 증식하는 좌표
    for second in range(1, s+1):
        now_queue = next_queue
        next_queue = deque()
        while now_queue:
            x, y = now_queue.popleft()
            # 현재 위치에서 4가지 방향으로의 위치 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 공간을 벗어나면 무시
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                # 방문기록이 없는데
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = virus
                    next_queue.append((nx, ny))
                # 바이러스 정보가 존재하는 경우
                else:
                    if matrix[nx][ny] < virus:
                        # 다른 바이러스와 비교 후 증식여부 판단
                        continue

# N, K 입력
n,k = map(int, input().split())

# NxN 형태의 시험관, 단, (1,1)이 시작점
matrix = []
viruses = [[] for _ in range(k+1)]

for i in range(1, n+1):
    input_list = list(map(int, input().split()))
    matrix.append(input_list)

    for j, value in enumerate(input_list):
        if value != 0:
            viruses[value] = [i,j+1]

# s초 뒤에 x,y 좌표
s,x,y = map(int, input().split())

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 시작
# 방문기록 초기화
for num, virus in enumerate(viruses):
    if len(virus) > 1:
        bfs(virus[0]-1, virus[1]-1, num)

print(matrix[x-1][y-1])