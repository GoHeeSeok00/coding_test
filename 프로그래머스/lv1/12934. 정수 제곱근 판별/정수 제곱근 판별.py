import math
def solution(n):
    answer = -1
    result = n ** 0.5
    if result == math.trunc(result):
        return (result + 1) ** 2
    return answer