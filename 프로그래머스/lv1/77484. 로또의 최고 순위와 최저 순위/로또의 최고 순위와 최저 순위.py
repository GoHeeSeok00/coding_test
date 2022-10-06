def solution(lottos, win_nums):
    score = 0
    zero_num = 0

    for lotto in lottos:
        if lotto == 0:
            zero_num += 1
        elif lotto in win_nums:
            score += 1

    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    answer = [rank[score+zero_num], rank[score]]

    return answer