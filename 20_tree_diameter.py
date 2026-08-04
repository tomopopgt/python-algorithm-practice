import sys
from collections import deque

def bfs(start, n, graph):
    """
    始点 start から各頂点への最短距離を計算し、
    (最も遠い頂点, その距離) を返す関数
    """
    dist = [-1] * n
    dist[start] = 0
    queue = deque([start])

    farthest_node = start
    max_dist = 0

    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                queue.append(v)
                if dist[v] > max_dist:
                    max_dist = dist[v]
                    farthest_node = v

    return farthest_node, max_dist


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    graph = [[] for _ in range(n)]

    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        graph[u].append((v, w))
        graph[v].append((u, w))
        idx += 3

    # 1回目の BFS: 任意の頂点 (0) から最も遠い頂点 s を探す
    s, _ = bfs(0, n, graph)

    # 2回目の BFS: 頂点 s から最も遠い頂点 t への距離を求める
    _, diameter = bfs(s, n, graph)

    # 直径を出力
    print(diameter)


if __name__ == '__main__':
    main()