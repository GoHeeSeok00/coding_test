def solution(n):
    str_n = str(n)
    list_n = []
    for i in str_n:
        list_n.append(i)
    list_n.sort(reverse=True)
    
    result = [str(integer) for integer in list_n]
    result_str = "".join(result)   
    return int(result_str)