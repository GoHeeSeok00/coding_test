def solution(arr):
    answer = []
    
    pop = arr.pop(0)
    answer.append(pop)
    
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    
    # for i, v in enumerate(arr):
    #     try:
    #         if v != arr[i+1]:
    #             answer.append(v)
    #     except IndexError:
    #         answer.append(v)
    return answer