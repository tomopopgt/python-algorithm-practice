import sys

class Edge:
    """
    残余グラフの辺を表す構造体
    """
    def __init__(self, to, cap, rev):
        self.to = to      # 行き先
        self.cap = cap    # 残り容量
        self.rev = rev    # 逆辺が相手の graph[to] のどこにあるかインデックス

class FordFulkerson:
    """
    Ford-Fulkerson アルゴリズムによる最大流クラス
    """
    def __init__(self, v):
        self.v = v
        self.graph = [[] for _ in range(v)]

    def add_edge(self, from_node, to_node, cap):
        """
        有向辺を追加する (同時に容量0の逆辺もセットで追加)
        """
        forward_idx = len(self.graph[from_node])
        backward_idx = len(self.graph[to_node])

        # 行きの辺
        self.graph[from_node].append(Edge(to_node, cap, backward_idx))
        # 帰りの辺 (残余グラフ用: 初期容量 0)
        self.graph[to_node].append(Edge(from_node, 0, forward_idx))

    def dfs(self, v, t, f, used):
        """
        DFS で増加パスを探索
        """
        if v == t:
            return f
        
        used[v] = True
        for edge in self.graph[v]:
            if not used[edge.to] and edge.cap > 0:
                # パス上の最小容量(ボトルネック)を計算
                d = self.dfs(edge.to, t, min(f, edge.cap), used)
                if d > 0:
                    # 正の流せる量が見つかったら容量を更新 (逆辺は加算)
                    edge.cap -= d
                    self.graph[edge.to][edge.rev].cap += d
                    return d
        return 0

    def max_flow(self, s, t):
        """
        s から t への最大流を計算
        """
        flow = 0
        while True:
            used = [False] * self.v
            f = self.dfs(s, t, float('inf'), used)
            if f == 0:
                # 増加パスが見つからなくなったら終了
                return flow
            flow += f


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    v = int(input_data[0])
    e = int(input_data[1])

    ff = FordFulkerson(v)
    idx = 2
    for _ in range(e):
        u = int(input_data[idx])
        to = int(input_data[idx+1])
        c = int(input_data[idx+2])
        ff.add_edge(u, to, c)
        idx += 3

    # 始点 0 から 終点 V-1 への最大流を出力
    print(ff.max_flow(0, v - 1))


if __name__ == '__main__':
    main()