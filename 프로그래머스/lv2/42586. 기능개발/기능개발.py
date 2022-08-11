from collections import deque


def solution(progresses, speeds):
    queue_progresses = deque(progresses)
    queue_speeds = deque(speeds)
    answer = []
    while queue_progresses:
        for i in range(len(queue_progresses)):
            queue_progresses[i] += queue_speeds[i]

        deploy = 0
        while queue_progresses:
            if queue_progresses[0] >= 100:
                queue_progresses.popleft()
                queue_speeds.popleft()
                deploy += 1
            else:
                if deploy > 0:
                    answer.append(deploy)
                deploy = 0
                break
        else:
            if deploy > 0:
                answer.append(deploy)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]