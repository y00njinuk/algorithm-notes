def solution(envelopes):
    envelopes.sort()
    d=[]
    d.append(envelopes[0])

    for i in range(1, len(envelopes)):
        x = envelopes[i][0]
        y = envelopes[i][1]

        for index, j in enumerate(d):
            chk = False
            if j[0] < x and j[1] < y:
                d[index] = envelopes[i]
                chk = True
                break
        
        if chk == False: 
            d.append(envelopes[i])

    answer = len(d)
    return answer

# array = [[3,5],[7,5],[3,3],[2,1]]
# array = [[3,4],[1,3],[2,5],[1,2],[3,5],[2,3]]
array = [[2,3],[4,5],[3,4]]
print(solution(array))

