import sys

# 再帰の上限を緩和
sys.setrecursionlimit(300000)

class BipartiteMatching:
    """
    二部グラフの最大マッチングクラス (DFSベース)
    """
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.graph = [[] for _ in range(x_size)]
        # match_y[v] : B 側の要素 v とマッチングしている A 側の要素 (未マッチングは -1)
        self.match_y = [-1] * y_size

    def add_edge(self, u, v):
        """
        A 側の u と B 側の v に辺を張る
        """
        self.graph[u].append(v)

    def _dfs(self, u, visited):
        """
        増加パスを探索する DFS
        """
        for v in self.graph[u]:
            if visited[v]:
                continue
            visited[v] = True

            # v が未マッチング、または v の現在のペアから別の増加パスが見つかる場合
            if self.match_y[v] < 0 or self._dfs(self.match_y[v], visited):
                self.match_y[v] = u
                return True
        return False

    def max_matching(self):
        """
        最大マッチング数を計算する (O(V * E))
        """
        res = 0
        for u in range(self.x_size):
            visited = [False] * self.y_size
            if self._dfs(u, visited):
                res += 1
        return res


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    x = int(input_data[0])
    y = int(input_data[1])
    e = int(input_data[2])

    bm = BipartiteMatching(x, y)

    idx = 3
    for _ in range(e):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        bm.add_edge(u, v)
        idx += 2

    print(bm.max_matching())


if __name__ == '__main__':
    main()