import sys

class RollingHash:
    """
    ローリングハッシュクラス (1D Rolling Hash)
    """
    def __init__(self, s, base=1007, mod=10**9 + 7):
        self.mod = mod
        n = len(s)
        self.hash = [0] * (n + 1)
        self.power = [1] * (n + 1)
        
        # 累積ハッシュと base の累乗テーブルを前計算 (O(N))
        for i in range(n):
            self.hash[i + 1] = (self.hash[i] * base + ord(s[i])) % mod
            self.power[i + 1] = (self.power[i] * base) % mod

    def get(self, l, r):
        """
        S[l:r] (半開区間 [l, r)) のハッシュ値を O(1) で取得
        """
        res = (self.hash[r] - self.hash[l] * self.power[r - l]) % self.mod
        return res


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = input_data[0]
    p = input_data[1]

    lt = len(t)
    lp = len(p)

    if lt < lp:
        return

    # テキストとパターンのローリングハッシュを生成
    rh_t = RollingHash(t)
    rh_p = RollingHash(p)

    # パターン P 全体のハッシュ値を取得
    p_hash = rh_p.get(0, lp)

    results = []
    # テキスト T 上を長さ |P| のウィンドウでスライドさせながら比較
    for i in range(lt - lp + 1):
        if rh_t.get(i, i + lp) == p_hash:
            results.append(str(i))

    if results:
        print('\n'.join(results))


if __name__ == '__main__':
    main()