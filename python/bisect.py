'''
순차 탐색 : 리스트 안에 특정한 데이터를 찾기 위해 앞에서부터 데이터를 탐색 
이진 탐색 : 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
- 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.
- 이진 탐색의 시간복잡도는 O(logN)이다
'''

'''
이진탐색 - 재귀함수 형태
'''
def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력받기
n, target = map(int ,input().split())
# 전체원소 입력받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)

'''
이진탐색 - 반복문 형태
'''
def binary_search2(array, target, start, end):
    while start<end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# n(원소의 개수)과 target(찾고자 하는 값)을 입력받기
n, target = map(int ,input().split())
# 전체원소 입력받기
array = list(map(int, input().split()))

result = binary_search2(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)