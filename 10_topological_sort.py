import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    graph = [[] for _ in range(n)]
    in_degree = [0] * n  # 各頂点の入次数 (自分に向かってくる矢印の数)

    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        graph[u].append(v)
        in_degree[v] += 1
        idx += 2

    # 1. 最初に入次数が 0 (前提条件なし) の頂点をキューに入れる
    # リスト内包表記で条件に合う要素を抽出
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    # 2. 幅優先探索 (BFS) ベースの Kahn アルゴリズム
    while queue:
        u = queue.popleft()
        result.append(str(u))

        # 頂点 u から伸びる矢印を取り除く
        for v in graph[u]:
            in_degree[v] -= 1
            # 入次数が 0 になったら (前提条件が全て揃ったら) キューに追加
            if in_degree[v] == 0:
                queue.append(v)

    # スペース区切りで一括出力
    print(' '.join(result))

if __name__ == '__main__':
    main()