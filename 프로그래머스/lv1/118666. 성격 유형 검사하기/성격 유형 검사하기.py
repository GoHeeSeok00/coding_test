def solution(survey, choices):
    answer = ""
    indicators = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    table = {1: [0, 3], 2: [0, 2], 3: [0, 1], 5: [1, 1], 6: [1, 2], 7: [1, 3]}
    rank = {} # {"R": 0, "T": 0, "C": 0,  "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    
    for i in indicators:
        rank.update({i[0]: 0, i[1]: 0})
    
    for category, choice in zip(survey, choices):
        if choice == 4:
            continue
        choice_table = table[choice] 
        rank[category[choice_table[0]]] += choice_table[1]
        
    for j in indicators:
        if rank[j[0]] >= rank[j[1]]:
            answer += j[0]
        else:
            answer += j[1]

    return answer