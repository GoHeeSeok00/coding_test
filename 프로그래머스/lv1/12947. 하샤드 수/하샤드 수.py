def solution(x):
    answer = True
    str_number = str(x)
    sum_number = 0
    
    for sn in str_number:
        sum_number += int(sn)
    
    if x % sum_number != 0:
        answer = False
    return answer