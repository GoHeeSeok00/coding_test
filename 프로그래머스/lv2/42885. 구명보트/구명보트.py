from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while people:  # 남아있는 사람이 있다면 반복
        if len(people) == 1: # 남은 사람이 한명이라면
            answer += 1
            break
        else:
            if people[0] > limit/2: # 가장 가벼운 사람 무게가 제한의 절반을 초과한 경우 (무조건 1명씩 탑승)
                answer += len(people)
                break
            
            if people[-1] <= limit/2: # 가장 무거운 사람 무게가 제한의 절반 이하인 경우 (무조건 2명씩 탑승)
                if len(people) % 2 == 0: # 남은 인워이 짝수인 경우
                    answer += int(len(people)/2)
                else: # 남은 인원이 홀수인 경우
                    answer += int(len(people)/2) + 1
                break
            
            if people[0] + people[-1] <= limit: # 가장 무거운 사람과 가장 가벼운 사람의 무게가 초과되지 않는다면
                people.popleft() # 가벼운사람
                people.pop() # 무거운사람
            else:
                people.pop()  # 가장 무거운 사람만 혼자 보트타기
            answer += 1    
        
    return answer