import sys

class SegmentTree:
    """
    点更新・区間最小値取得 (RMQ) セグメントツリー
    """
    def __init__(self, size, default=float('inf')):
        self.n = 1
        while self.n < size:
            self.n *= 2
        self.default = default
        # 1-indexed 管理のためのサイズ 2 * n の配列
        self.tree = [default] * (2 * self.n)

    def build(self, arr):
        """
        初期配列から O(N) でセグメントツリーを構築
        """
        for i, v in enumerate(arr):
            self.tree[self.n + i] = v
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i, val):
        """
        A[i] を val に更新 (O(log N))
        """
        idx = self.n + i
        self.tree[idx] = val
        while idx > 1:
            idx //= 2
            self.tree[idx] = min(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, l, r):
        """
        半開区間 [l, r) の最小値を求める (O(log N))
        """
        res_l = self.default
        res_r = self.default
        l += self.n
        r += self.n

        while l < r:
            # l が右側の子(奇数インデックス)ならそのノードを採用して右へ進める
            if l & 1:
                res_l = min(res_l, self.tree[l])
                l += 1
            # r が右側の子ならその1つ左(偶数)のノードを採用する
            if r & 1:
                r -= 1
                res_r = min(res_r, self.tree[r])
            l //= 2
            r //= 2

        return min(res_l, res_r)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    a = [int(x) for x in input_data[2 : 2 + n]]

    seg = SegmentTree(n)
    seg.build(a)

    results = []
    idx = 2 + n
    for _ in range(q):
        t = int(input_data[idx])
        p1 = int(input_data[idx+1])
        p2 = int(input_data[idx+2])
        idx += 3

        if t == 0:
            seg.update(p1, p2)
        elif t == 1:
            res = seg.query(p1, p2)
            results.append(str(res))

    print('\n'.join(results))


if __name__ == '__main__':
    main()