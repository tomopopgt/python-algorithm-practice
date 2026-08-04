import sys

class UnionFind:
    """
    素集合データ構造 (Union-Find)
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            return True
        return False


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    v = int(input_data[0])
    e = int(input_data[1])

    edges = []
    idx = 2
    for _ in range(e):
        u = int(input_data[idx])
        to = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((w, u, to))
        idx += 3

    # 1. 辺をコスト w の昇順にソート (O(E log E))
    edges.sort()

    uf = UnionFind(v)
    mst_cost = 0
    edges_count = 0

    # 2. コストが低い辺から順に評価
    for w, u, to in edges:
        # u と to がまだ連結されていない場合のみ採用 (閉路回避)
        if uf.union(u, to):
            mst_cost += w
            edges_count += 1
            # V-1 本の辺を選んだ時点で最小全域木が完成
            if edges_count == v - 1:
                break

    print(mst_cost)


if __name__ == '__main__':
    main()