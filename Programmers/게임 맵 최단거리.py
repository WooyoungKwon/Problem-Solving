from collections import deque
def solution(n, wires):
    answer = n
    # wires를 2차원 배열로 표현, 1번 송전탑부터 시작이기 때문에 n+1
    tree = [[] for _ in range(n+1)]
    # 송전탑 간의 간선을 트리로 구현
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)

    for start, split in wires:
        visited = [False] * (n+1)
        # bfs는 모든 노드를 순회하여 count를 세는 방식인데, 간선을 끊기 위해 split 노드를 이미 방문함으로 처리하여 bfs에 내에서 순회하지 않는 방식으로 간선을 끊었음.
        visited[split] = True
        cnt = bfs(start, visited, tree)
        if answer > abs(cnt - (n - cnt)):
            answer = abs(cnt - (n - cnt))
    return answer

def bfs(start, visited, tree):
    cnt = 1
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = True
            cnt += 1
    return cnt
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
