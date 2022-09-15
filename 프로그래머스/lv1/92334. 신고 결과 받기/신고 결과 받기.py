# 각 유저는 한명의 유저를 신고 여러번 신고해도 1회 처리
# k번 이상 신고된 유저는 이용 정지 - 신고한 유저에게 메일 발송
def solution(id_list, report, k):
    report_dict = {}

    id_dict = {}
    for id in id_list:
        id_dict[id] = 0


    for i in report:
        result = i.split(' ')
        try:
            report_list = report_dict[result[1]]
            if result[0] not in report_list:
                report_list.append(result[0])
                report_dict[result[1]] = report_list
            else: # 해당 유저를 신고한 유저 목록에 현재 신고 접수한 유저가 있으면 pass
                # print(f'{result[0]}는 이미 {result[1]}를 신고했습니다.')
                pass

        except KeyError:
            report_dict[result[1]] = [result[0]]


    for key, value in report_dict.items():
        if len(value) >= k:
            for v in value:
                id_dict[v] += 1

    return list(id_dict.values())