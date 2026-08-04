import sys

# 深い再帰処理に備えて上限を緩和
sys.setrecursionlimit(300000)

class LazySegmentTree:
    """
    区間加算・区間和取得 (RAQ + RSQ) 遅延評価セグメントツリー
    """
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        # 値を保持する木構造配列
        self.tree = [0] * (2 * self.size)
        # 遅延値を保持する配列
        self.lazy = [0] * (2 * self.size)

    def _eval(self, k, l, r):
        """
        ノード k に溜まっている遅延値を評価し、子ノードへ伝播する
        """
        if self.lazy[k] != 0:
            # 区間の長さを掛け合わせた値を自身のノードに反映
            self.tree[k] += self.lazy[k] * (r - l)
            if r - l > 1:
                # 子ノード(左右)へ遅延値を引き継ぐ
                self.lazy[2 * k] += self.lazy[k]
                self.lazy[2 * k + 1] += self.lazy[k]
            # 自身の遅延値をリセット
            self.lazy[k] = 0

    def add(self, a, b, x, k=1, l=0, r=None):
        """
        半開区間 [a, b) のすべての要素に x を加算 (O(log N))
        """
        if r is None:
            r = self.size

        self._eval(k, l, r)

        # 完全に枠外の場合は何もしない
        if b <= l or r <= a:
            return

        # 完全に区間に包摂される場合は遅延値に乗せて打ち切り
        if a <= l and r <= b:
            self.lazy[k] += x
            self._eval(k, l, r)
            return

        mid = (l + r) // 2
        self.add(a, b, x, 2 * k, l, mid)
        self.add(a, b, x, 2 * k + 1, mid, r)
        self.tree[k] = self.tree[2 * k] + self.tree[2 * k + 1]

    def query(self, a, b, k=1, l=0, r=None):
        """
        半開区間 [a, b) の総和を取得 (O(log N))
        """
        if r is None:
            r = self.size

        self._eval(k, l, r)

        if b <= l or r <= a:
            return 0

        if a <= l and r <= b:
            return self.tree[k]

        mid = (l + r) // 2
        res_l = self.query(a, b, 2 * k, l, mid)
        res_r = self.query(a, b, 2 * k + 1, mid, r)
        return res_l + res_r


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    lazy_seg = LazySegmentTree(n)

    results = []
    idx = 2
    for _ in range(q):
        t = int(input_data[idx])
        if t == 0:
            l = int(input_data[idx+1])
            r = int(input_data[idx+2])
            x = int(input_data[idx+3])
            lazy_seg.add(l, r, x)
            idx += 4
        elif t == 1:
            l = int(input_data[idx+1])
            r = int(input_data[idx+2])
            res = lazy_seg.query(l, r)
            results.append(str(res))
            idx += 3

    print('\n'.join(results))


if __name__ == '__main__':
    main()