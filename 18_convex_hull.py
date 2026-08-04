import sys

def cross_product(o, a, b):
    """
    ベクトル OA と ベクトル OB の外積 (Cross Product) を計算
    > 0  : 反時計回り (左折)
    < 0  : 時計回り (右折)
    == 0 : 一直線上に存在する
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    points = []
    idx = 1
    for _ in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        points.append((x, y))
        idx += 2

    # 1. 点を x 座標昇順 (同値なら y 座標昇順) にソート
    points.sort()

    # 2. 下側凸包 (Lower Hull) の構築
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # 3. 上側凸包 (Upper Hull) の構築
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # 4. 重複する端点を取り除いて結合
    hull = lower[:-1] + upper[:-1]

    # 結果の出力
    print(len(hull))
    for x, y in hull:
        print(f"{x} {y}")

if __name__ == '__main__':
    main()