from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_in_bridge = deque()
    truck_weights = deque(truck_weights)
    truck_in_bridge.append([truck_weights.popleft(), 1])
    now_weights = truck_in_bridge[0][0]
    
    while truck_in_bridge:
        if truck_in_bridge[0][1] == bridge_length:
            pop_bridge = truck_in_bridge.popleft()
            now_weights -= pop_bridge[0]

        if truck_weights:
            if now_weights + truck_weights[0] <= weight:
                truck_in_bridge.append([truck_weights.popleft(), 0])
                now_weights += truck_in_bridge[-1][0]

        for truck in truck_in_bridge:
            truck[1] += 1

        answer += 1
    return answer
