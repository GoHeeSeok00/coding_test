from collections import deque


def solution(priorities, location):
    answer = 0
    tasks = deque()
    
    for i, v in enumerate(priorities):
        if i == location:
            tasks.append([1, v])
        tasks.append([0, v])
    
    while tasks:
        take_out = tasks.popleft()
        take_out_priorities = take_out[1]
        for task in tasks:
            if take_out_priorities < task[1]:
                take_out_priorities = task[1]
        if take_out_priorities != take_out[1]:
            tasks.append(take_out)
        else:
            answer += 1
            if take_out[0] == 1:
                return answer
            
        