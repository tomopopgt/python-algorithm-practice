import sys

class BinaryIndexedTree:
    """
    Binary Indexed Tree (Fenwick Tree / BIT)
    1-indexed で内部処理を行う点加算・区間和データ構造
    """
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, x):
        """
        A[i] に x を加算 (i は 0-indexed)
        """
        idx = i + 1
        while idx <= self.n:
            self.tree[idx] += x
            idx += idx & (-idx)  # 最下位ビット (LSB) を加えて親方向へ進む

    def _sum(self, i):
        """
        A[0] から A[i-1] までの累積和を取得 (i 個分の和)
        """
        s = 0
        idx = i
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)  # 最下位ビット (LSB) を引いて親方向へ遡る
        return s

    def query(self, l, r):
        """
        半開区間 [l, r) の総和を取得
        """
        return self._sum(r) - self._sum(l)


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    bit = BinaryIndexedTree(n)

    # 初期配列の要素を BIT にセット
    for i in range(n):
        bit.add(i, int(input_data[2 + i]))

    results = []
    idx = 2 + n
    for _ in range(q):
        t = int(input_data[idx])
        p1 = int(input_data[idx+1])
        p2 = int(input_data[idx+2])
        idx += 3

        if t == 0:
            bit.add(p1, p2)
        elif t == 1:
            res = bit.query(p1, p2)
            results.append(str(res))

    print('\n'.join(results))


if __name__ == '__main__':
    main()