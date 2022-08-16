def solution(rows, columns, queries):
    answer = []
    # 1. 행렬 만들기
    procession = []
    for i in range(rows):
        procession.append(list(range((columns * i) + 1, (columns * i) + columns + 1)))
    print(procession)

    # queries [[x1, y1, x2, y2]]
    #           0   1   2   3
    # (x1, y1) ~ (x1, y2) 오른쪽으로 한칸 이동
    # (x1, y2) ~ (x2, y2) 아래쪽으로 한칸 이동
    # (x2, y2) ~ (x2, y1) 왼쪽으로 한칸 이동
    # (x2, y1) ~ (x1, y1) 위쪽으로 한칸 이동

    # 2. 위치 이동
    for query in queries:
        x1 = query[0]-1
        y1 = query[1]-1
        x2 = query[2]-1
        y2 = query[3]-1
        
        # 타겟 대상 저장
        target_list = []
        target = procession[x1][y1]
        # print(f"target : {target}")
        
        # 오른쪽 이동
        for i in range(1, (y2 - y1) + 1):
            procession[x1][y1 + i], target = target, procession[x1][y1 + i]
            target_list.append(target)

        # 아래로 이동
        for i in range(1, (x2 - x1) + 1):
            procession[x1 + i][y2], target = target, procession[x1 + i][y2]
            target_list.append(target)
        # 왼쪽 이동
        for i in range(1, (y2 - y1) + 1):
            procession[x2][y2 - i], target = target, procession[x2][y2 - i]
            target_list.append(target)

        # 아래로 이동
        for i in range(1, (x2 - x1) + 1):
            procession[x2 - i][y1], target = target, procession[x2 - i][y1]
            target_list.append(target)
            
        # 타겟 대상중 가장 작은 타겟 answer 변수에 추가    
        answer.append(min(target_list))
        # print(f"procession : {procession}")
    return answer