def solutions(mails, period, K):
    result = 0
    for i in range(0, len(mails)-period+1):
        total = sum(mails[i:(i+period)])//period
        if total >= int(K):
            result += 1

    answer = result
    return answer

print(solutions([9,20,10,30,23,4], 3, 20))