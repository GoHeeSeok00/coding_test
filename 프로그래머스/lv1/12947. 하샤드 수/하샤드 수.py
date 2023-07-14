def solution(x):
    str_number = str(x)
    sum_number = 0
    
    for sn in str_number:
        sum_number += int(sn)

    return x % sum_number == 0