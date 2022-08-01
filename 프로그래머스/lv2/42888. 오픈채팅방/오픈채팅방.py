def solution(records):
    answer = [] # 정답
    id_mapping_nickname = {} # id와 nickname 매핑 딕셔너리
    id_record_list = []
    for record in records:
        results = record.split(" ")
        id = results[1]
        if results[0] == "Enter":
            # id와 nickname 매핑
            id_mapping_nickname[id] = results[2]
            id_record_list.append(f"E {id}")
            
        elif results[0] == "Change":
            # id와 nickname 매핑
            id_mapping_nickname[id] = results[2]
            
        else:
            id_record_list.append(f"L {id}")
    
    for record in id_record_list:
        results = record.split(" ")
        id = results[1]
        if results[0] == "E":
            answer.append(f"{id_mapping_nickname[id]}님이 들어왔습니다.")
        else:
            answer.append(f"{id_mapping_nickname[id]}님이 나갔습니다.")    
    return answer