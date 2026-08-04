import sys

# 深い DFS に備えて再帰上限を緩和
sys.setrecursionlimit(300000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    v = int(input_data[0])
    e = int(input_data[1])

    graph = [[] for _ in range(v)]
    rev_graph = [[] for _ in range(v)]

    idx = 2
    for _ in range(e):
        u = int(input_data[idx])
        to = int(input_data[idx+1])
        graph[u].append(to)
        rev_graph[to].append(u)  # 辺を逆張りしたグラフも作成
        idx += 2

    # 1. 第 1 パス: 順方向グラフで DFS し、帰還順 (order) を記録
    visited = [False] * v
    order = []

    def dfs1(u):
        visited[u] = True
        for to in graph[u]:
            if not visited[to]:
                dfs1(to)
        order.append(u)

    for i in range(v):
        if not visited[i]:
            dfs1(i)

    # 2. 第 2 パス: 帰還順の逆順から、逆方向グラフで DFS を行って強連結成分を抽出
    visited2 = [False] * v
    components = []

    def dfs2(u, comp):
        visited2[u] = True
        comp.append(u)
        for to in rev_graph[u]:
            if not visited2[to]:
                dfs2(to, comp)

    for u in reversed(order):
        if not visited2[u]:
            comp = []
            dfs2(u, comp)
            comp.sort()  # グループ内を昇順ソート
            components.append(comp)

    # 3. 結果の出力
    print(len(components))
    for comp in components:
        print(" ".join(map(str, comp)))


if __name__ == '__main__':
    main()