import sys
import heapq

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])

    # 隣接リストの構築
    graph = [[] for _ in range(n)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        graph[u].append((v, w))
        idx += 3

    # 最短距離配列 (無限大で初期化)
    dist = [float('inf')] * n
    dist[s] = 0

    # 優先度付きキュー (コスト, 頂点) のタプルを格納
    pq = [(0, s)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # 既に求めた距離より大きければスキップ (枝刈り)
        if current_dist > dist[u]:
            continue

        # 隣接する頂点の更新
        for v, cost in graph[u]:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                heapq.heappush(pq, (dist[v], v))

    # 結果の出力
    results = []
    for d in dist:
        if d == float('inf'):
            results.append("-1")
        else:
            results.append(str(d))

    print('\n'.join(results))

if __name__ == '__main__':
    main()