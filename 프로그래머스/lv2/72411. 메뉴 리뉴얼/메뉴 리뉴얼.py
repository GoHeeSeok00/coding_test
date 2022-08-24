from itertools import combinations


def solution(orders, course):
    answer = []
    result_list = []
    for c in course:
        for order in orders:
            result_list += list(combinations(sorted(order), c))
        result_count = []
        max_cnt = 0
        for result in result_list:
            cnt = result_list.count(result)
            result_count.append(cnt)
            if max_cnt < cnt:
                max_cnt = cnt
        if max_cnt >= 2:
            max_cnt_result = []
            for i, v in enumerate(result_count):
                if v == max_cnt:
                    max_cnt_result.append(result_list[i])
            max_cnt_result = set(max_cnt_result)
            for m in max_cnt_result:
                answer.append("".join(m))

        result_list.clear()
    answer.sort()
    return answer