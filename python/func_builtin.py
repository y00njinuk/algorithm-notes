# 중위표기법
result = eval("(3+7+4)*3")
print(result)

# 순열
from itertools import permutations
data = ['A', 'B', 'C']
print(list(permutations(data, 3))) # 3P3
print(list(permutations(data, 2))) # 3P2
print(list(permutations(data, 1))) # 3P1

# 조합
from itertools import combinations
data = ['A', 'B', 'C']
print(list(combinations(data, 3))) # 3C3
print(list(combinations(data, 2))) # 3C2
print(list(combinations(data, 1))) # 3C1

# 중복순열
from itertools import product
data = ['A', 'B', 'C']
# 2개를 뽑는 모든 순열 (중복 O)
print(list(product(data, repeat=2)))

# 중복조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
# 2개를 뽑는 모든 조합 (중복 O)
print(list(combinations_with_replacement(data, 2)))