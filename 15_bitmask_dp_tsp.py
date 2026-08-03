import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    # 距離行列の取得
    dist = []
    idx = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input_data[idx]))
            idx += 1
        dist.append(row)

    # dp[mask][u] : 訪問状態 mask, 現在地 u における最小コスト
    # mask: 0 ~ (1 << n) - 1
    inf = float('inf')
    dp = [[inf] * n for _ in range(1 << n)]

    # 初期状態: 都市 0 のみ訪問済み (1 << 0 = 1), 現在地は 0
    dp[1][0] = 0

    # すべての集合状態を順に処理
    for mask in range(1, 1 << n):
        for u in range(n):
            if dp[mask][u] == inf:
                continue

            # 次の都市 v へ移動を試みる
            for v in range(n):
                # すでに訪問済みならスキップ (v ビット目が 1 かどうか)
                if (mask >> v) & 1:
                    continue

                # 都市 v を訪問済みにした次の状態
                next_mask = mask | (1 << v)
                if dp[mask][u] + dist[u][v] < dp[next_mask][v]:
                    dp[next_mask][v] = dp[mask][u] + dist[u][v]

    # 全都市訪問済み (all_visited) の状態から、最後に都市 0 へ戻るコストを計算
    all_visited = (1 << n) - 1
    ans = inf
    for u in range(n):
        if dp[all_visited][u] != inf:
            ans = min(ans, dp[all_visited][u] + dist[u][0])

    if ans == inf:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()