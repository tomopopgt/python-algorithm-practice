import sys

class UnionFind:
    """
    Union-Find (Disjoint Set Union) クラス
    """
    def __init__(self, n):
        # 各要素の親ノード (初期状態は自分自身が親)
        self.parent = list(range(n))
        # 木の高さ (ランク) の初期値は 0
        self.rank = [0] * n

    def find(self, x):
        """
        要素 x の属するグループの代表(根)を返す (経路圧縮つき)
        """
        if self.parent[x] == x:
            return x
        # 再帰的に根を探しつつ、直接根に繋ぎ直す (経路圧縮)
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        要素 x と要素 y の属するグループを統合する (Union by Rank)
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # ランクが低い方の木を、高い方の木の下に結合
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            
            # 高さが同じ場合は統合後のランクを 1 増やす
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def same(self, x, y):
        """
        要素 x と要素 y が同じグループに属しているか判定
        """
        return self.find(x) == self.find(y)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    uf = UnionFind(n)
    results = []
    idx = 2

    for _ in range(q):
        t = int(input_data[idx])
        u = int(input_data[idx+1])
        v = int(input_data[idx+2])
        idx += 3

        if t == 0:
            uf.union(u, v)
        elif t == 1:
            if uf.same(u, v):
                results.append("1")
            else:
                results.append("0")

    print('\n'.join(results))


if __name__ == '__main__':
    main()