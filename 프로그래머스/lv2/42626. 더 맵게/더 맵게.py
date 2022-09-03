import heapq


def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)

    if heap[0] >= K:
        return answer

    while len(heap) >= 2:
        item1 = heapq.heappop(heap)
        item2 = heapq.heappop(heap)
        heapq.heappush(heap, item1 + (item2 * 2))
        answer += 1
        if heap[0] >= K:
            return answer

    else:
        return -1