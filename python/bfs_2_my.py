def minimum_distance(graph, start, distance=1):
    for node in graph:
        if start == node[0]:
            if cities[start-1][0] == x:
                minimum_distance(graph, node[1], distance)
            else:
                cities[start-1][1] += distance
                distance += 1
                minimum_distance(graph, node[1], distance)
                distance = 1

    if cities[start-1][1] == 0:
        cities[start-1][1] = distance
    elif cities[start-1][1] != 0 and cities[start-1][1] > distance:
        cities[start-1][1] = distance
    return 

# Input Variable
n,m,k,x = map(int, input().split())
cities  = [[i,0] for i in range(1,n+1)] 
graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))

minimum_distance(graph, x)

for city in cities:
    if city[1] == k:
        print(city[0], end=' ')

'''
문제점1) (출발지, 목적지) 정보를 그대로 리스트 형태로 저장
문제점2) 그대로 리스트에 저장하여 재귀함수 형태로 풀어나감
문제점3) 최소 길이로 방문한 노드에 대해서도 계속 접근
'''