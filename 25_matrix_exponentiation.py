import sys

MOD = 10**9 + 7

def multiply_matrix(a, b):
    """
    2x2 行列の積 (A * B) % MOD を計算する関数
    """
    c = [[0, 0], [0, 0]]
    c[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD
    c[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD
    c[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD
    c[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD
    return c


def power_matrix(a, n):
    """
    繰り返し二乗法による 2x2 行列 A^n % MOD の計算 (O(log N))
    """
    # 単位行列 E で初期化
    res = [[1, 0], [0, 1]]
    base = a

    while n > 0:
        if n & 1:
            res = multiply_matrix(res, base)
        base = multiply_matrix(base, base)
        n >>= 1

    return res


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    if n == 0:
        print(0)
        return
    elif n == 1:
        print(1)
        return

    # 遷移行列 A = [[1, 1], [1, 0]]
    a = [[1, 1], [1, 0]]

    # A^(n-1) を計算
    res_matrix = power_matrix(a, n - 1)

    # (F_n, F_(n-1))^T = A^(n-1) * (F_1, F_0)^T
    # F_1 = 1, F_0 = 0 より、F_n は res_matrix[0][0] に格納される
    print(res_matrix[0][0])


if __name__ == '__main__':
    main()