def solution(arr):
    if len(arr) == 1:
        return [-1]
    min_index = 0
    for i, v in enumerate(arr):
        if arr[min_index] > v:
            min_index = i
    arr.pop(min_index)
    return arr