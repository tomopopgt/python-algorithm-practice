import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            return True  # 結合に成功した（元々別グループだった）
        return False     # 既に同じグループだった（閉路になるので結合しない）


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    # 辺情報を (コスト, 頂点u, 頂点v) のリストとして読み込む
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        edges.append((w, u, v))
        idx += 3

    # コスト w を基準に昇順ソート (Python はタプルの1番目の要素で自動ソートしてくれる)
    edges.sort()

    uf = UnionFind(n)
    total_cost = 0
    edge_count = 0

    for w, u, v in edges:
        # 2頂点がまだ繋がっていない場合のみ採用
        if uf.union(u, v):
            total_cost += w
            edge_count += 1
            # N - 1 本の辺を選んだ時点で全域木が完成するので即時終了 (枝刈り)
            if edge_count == n - 1:
                break

    print(total_cost)


if __name__ == '__main__':
    main()