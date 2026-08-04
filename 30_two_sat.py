import sys

# 再帰深度の制限を緩和
sys.setrecursionlimit(300000)

class TwoSAT:
    """
    2-SAT (2-Satisfiability) ソルバー (SCCベース)
    """
    def __init__(self, n):
        self.n = n
        self.num_vertices = 2 * n
        self.graph = [[] for _ in range(self.num_vertices)]
        self.rev_graph = [[] for _ in range(self.num_vertices)]

    def _neg(self, u):
        """
        リテラル u の否定ノード番号を取得
        """
        return u + self.n if u < self.n else u - self.n

    def add_clause(self, u, u_neg, v, v_neg):
        """
        条件 (u_val or v_val) を追加
        u_neg / v_neg が True なら否定 (not)
        """
        node_u = u + self.n if u_neg else u
        node_v = v + self.n if v_neg else v

        neg_u = self._neg(node_u)
        neg_v = self._neg(node_v)

        # (A or B) <=> (not A -> B) and (not B -> A)
        self.graph[neg_u].append(node_v)
        self.graph[neg_v].append(node_u)

        self.rev_graph[node_v].append(neg_u)
        self.rev_graph[node_u].append(neg_v)

    def solve(self):
        """
        2-SAT を解き、(満足可能か, 各変数の割り当てリスト) を返す
        """
        # 1. 1回目の DFS (帰還順記録)
        visited = [False] * self.num_vertices
        order = []

        def dfs1(u):
            visited[u] = True
            for to in self.graph[u]:
                if not visited[to]:
                    dfs1(to)
            order.append(u)

        for i in range(self.num_vertices):
            if not visited[i]:
                dfs1(i)

        # 2. 2回目の DFS (逆グラフで SCC 分解)
        visited2 = [False] * self.num_vertices
        comp_id = [-1] * self.num_vertices
        current_comp = 0

        def dfs2(u, cid):
            visited2[u] = True
            comp_id[u] = cid
            for to in self.rev_graph[u]:
                if not visited2[to]:
                    dfs2(to, cid)

        for u in reversed(order):
            if not visited2[u]:
                dfs2(u, current_comp)
                current_comp += 1

        # 3. 矛盾判定と解の決定
        ans = [0] * self.n
        for i in range(self.n):
            # x_i と not x_i が同じ SCC に属していれば矛盾 (充当不能)
            if comp_id[i] == comp_id[i + self.n]:
                return False, []
            # トポロジカル順序で下流 (comp_id が大きい) 方を 1 (True) に採用
            ans[i] = 1 if comp_id[i] > comp_id[i + self.n] else 0

        return True, ans


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    sat = TwoSAT(n)

    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        u_neg = bool(int(input_data[idx+1]))
        v = int(input_data[idx+2])
        v_neg = bool(int(input_data[idx+3]))
        sat.add_clause(u, u_neg, v, v_neg)
        idx += 4

    possible, assignment = sat.solve()

    if possible:
        print("POSSIBLE")
        print(" ".join(map(str, assignment)))
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()