import sys
from collections import deque

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
        graph[u].append(v)
        graph[v].append(u)
        idx += 2

    # 1. 各頂点の深さと 1つ上の親を BFS で求める
    depth = [-1] * n
    # parent[k][u] : 頂点 u の 2^k 個上の親 (今回は 2^20 > 500,000 まで確保)
    max_k = 20
    parent = [[-1] * n for _ in range(max_k)]

    depth[0] = 0
    queue = deque([0])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if depth[v] == -1:
                depth[v] = depth[u] + 1
                parent[0][v] = u
                queue.append(v)

    # 2. ダブリングテーブルの構築 (2^k 先の親は、2^(k-1) 先の親の 2^(k-1) 先の親)
    for k in range(max_k - 1):
        for u in range(n):
            if parent[k][u] != -1:
                parent[k + 1][u] = parent[k][parent[k][u]]

    # 3. LCA クエリ関数 (O(log N))
    def get_lca(u, v):
        # u の方が深い状態にする
        if depth[u] < depth[v]:
            u, v = v, u

        # 深さの差を 2^k ステップで縮めて揃える
        diff = depth[u] - depth[v]
        for k in range(max_k):
            if (diff >> k) & 1:
                u = parent[k][u]

        # 深さを揃えた時点で同じ頂点ならそれが LCA
        if u == v:
            return u

        # 親が一致する直前まで同時に遡る
        for k in range(max_k - 1, -1, -1):
            if parent[k][u] != parent[k][v]:
                u = parent[k][u]
                v = parent[k][v]

        return parent[0][u]

    # クエリ処理
    q = int(input_data[idx])
    idx += 1

    results = []
    for _ in range(q):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        results.append(str(get_lca(u, v)))

    print('\n'.join(results))

if __name__ == '__main__':
    main()