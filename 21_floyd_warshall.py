import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    v = int(input_data[0])
    e = int(input_data[1])

    inf = float('inf')
    # dp[i][j] : 頂点 i から 頂点 j への最短距離
    dp = [[inf] * v for _ in range(v)]

    # 自分自身への距離は 0 で初期化
    for i in range(v):
        dp[i][i] = 0

    idx = 2
    for _ in range(e):
        u = int(input_data[idx])
        to = int(input_data[idx+1])
        w = int(input_data[idx+2])
        # 多重辺がある場合は最小値を保持
        dp[u][to] = min(dp[u][to], w)
        idx += 3

    # フロイド・ワーシャル法 (O(V^3))
    # 中間経由地 k を最外ループにするのが最重要ポイント！
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dp[i][k] != inf and dp[k][j] != inf:
                    if dp[i][k] + dp[k][j] < dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k][j]

    # 負の閉路の検出 (自分自身への距離 dp[i][i] が負になっていれば負回路が存在)
    for i in range(v):
        if dp[i][i] < 0:
            print("NEGATIVE CYCLE")
            return

    # 結果の出力
    for i in range(v):
        row = []
        for j in range(v):
            if dp[i][j] == inf:
                row.append("INF")
            else:
                row.append(str(dp[i][j]))
        print(" ".join(row))


if __name__ == '__main__':
    main()