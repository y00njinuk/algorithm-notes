'''
파이썬 이진 탐색 라이브러리
- bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 위치를 반환
- bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 위치를 반환
'''
# from bisect import bisect_left, bisect_right

# a = [1, 2, 4, 4, 8]
# x = 4
# print(bisect_left(a, x))
# print(bisect_right(a, x))

'''
값이 특정 범위에 속하는 데이터 개수 구하기
'''
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a, 4, 4)) # 값이 4인 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 값이 [-1, 3] 범위에 있는 데이터 개수 출력