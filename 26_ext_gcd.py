import sys

def ext_gcd(a, b):
    """
    拡張ユークリッドの互除法
    a * x + b * y = gcd(a, b) となる (gcd, x, y) を返す
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = ext_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, m):
    """
    a の mod m における逆元 (a * x ≡ 1 mod m) を求める
    """
    g, x, _ = ext_gcd(a, m)
    if g != 1:
        return -1  # gcd(a, m) != 1 の場合、逆元は存在しない

    # x が負の値になる場合があるため、正の最小剰余に変換
    return (x % m + m) % m


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    a = int(input_data[0])
    m = int(input_data[1])

    ans = mod_inverse(a, m)
    print(ans)


if __name__ == '__main__':
    main()