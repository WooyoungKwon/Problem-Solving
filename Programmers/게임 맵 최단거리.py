from collections import deque
def solution(maps):
        answer = 0
        # 상하좌우
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        queue = deque()
        # 0, 0에서 시작한다.
        queue.append((0,0))
        
        while queue:
                x, y = queue.popleft()
                for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        # 가로, 세로 길이
                        N = len(maps)
                        M = len(maps[0])
                        if 0<=nx<N and 0<=ny<M and maps[nx][ny] == 1:
                                # 방문한 곳은 1로 바꿔줌
                                maps[nx][ny] = maps[x][y] + 1
                                # 방문한 곳을 큐에 추가하여 다음 반복 때 기준으로 삼고 주변 노드 탐색
                                queue.append((nx, ny))
        answer = maps[N-1][M-1]

        if answer == 1:
                answer = -1
        return answer
