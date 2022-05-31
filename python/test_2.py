def solution(s):
    d = [0] * len(s)
    d[0] = 0

    for i in range(1, len(s)):
        if i % 2 == 0:
            if s[i-1] < s[i]:
                d[i] = d[i-1] + 1
            else:
                d[i] = d[i-1]
        
        else:
            if s[i-1] > s[i]:
                d[i] = d[i-1] + 1
            else:
                d[i] = d[i-1]

    answer = d[len(s)-1]
    return answer

# print(solution([1,2,3]))
print(solution([3,-1,0,4]))