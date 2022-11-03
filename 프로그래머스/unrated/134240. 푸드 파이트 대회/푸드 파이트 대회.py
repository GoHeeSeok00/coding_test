def solution(food):
    a = ""
    for i, v in enumerate(food[1:]):
        cnt = v // 2
        a += f'{i+1}' * cnt
    return a + "0" + a[::-1]