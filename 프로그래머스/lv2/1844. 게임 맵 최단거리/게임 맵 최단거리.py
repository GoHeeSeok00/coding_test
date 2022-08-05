from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        # 큐에 사용자 위치 추가
        queue = deque()
        queue.append((x, y))
        # 큐가 빌때까지 반복
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 맵 벗어나면 무시
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 벽이면 무시
                if maps[nx][ny] == 0:
                    continue
                # 처음 방문한 곳이라면
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] += maps[x][y]
    bfs(0, 0)
    answer = maps[n - 1][m - 1]
    if answer == 1:
        return -1
    return answer