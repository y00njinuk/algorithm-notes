'''
정렬(Sorting) : 데이터를 특정한 기준에 따라 순서대로 나열하는 것
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됩니다.
'''

'''
1. 선택정렬 : 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복하는 정렬
-> 시간복잡도 : O(n2)
'''
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i # 가장 작은 원소에 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # Swap
print(array)

'''
2. 삽입정렬 : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
- 선택정렬에 비해 구현 난이도가 높지만, 일반적으로 더 효율적으로 동작한다.
- Why? 이미 정렬이 되어있는 상태에서 다시 정렬을 한다면 선택정렬보다 더 빠르다
- 즉, 최선의 경우 시간복잡도가 O(n)이다
'''
array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break # 삽입 지점이 더 이상 없음 (앞 데이터가 더 작기 때문)
print(array)

'''
3. 퀵정렬 : 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘이다
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 된다
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정한다.
- 퀵 정렬은 평균의 경우 O(NlongN)의 시간복잡도를 가진다.
- 하지만 최악의 경우 시간복잡도가 O(N2)이다.
'''
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left<=right:
        while left<=end and array[left]<=array[pivot]:
            left += 1
        while right>start and array[right]>=array[pivot]:
            right -=1
        if left>right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 파이썬의 장점을 살린 방식 - 리스트 컴프리핸션 이용
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort2(array):
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트
    left_side = [x for x in tail if x<=pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x>pivot] # 분할된 오른쪽 부분 

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)
print(quick_sort2(array))

'''

'''