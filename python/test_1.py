def solution(arr):
    set_arr = set(arr[0]+arr[1]+arr[2])
    for element in set_arr:
        x_chk=0
        y_chk=0
        for i in range(3):
            if arr[i][0] == element:
                x_chk += 1
            elif arr[i][1] == element:
                y_chk += 1
        if x_chk == 1:
            x = element
        elif y_chk == 1:
            y = element
            
    answer = [x, y]
    return answer

arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))
    
print(solution(arr))