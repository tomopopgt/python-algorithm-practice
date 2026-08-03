import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    max_w = int(input_data[1])

    items = []
    idx = 2
    for _ in range(n):
        v = int(input_data[idx])
        w = int(input_data[idx+1])
        items.append((v, w))
        idx += 2

    # 1次元配列 DP の初期化 (重さ j における最大価値)
    dp = [0] * (max_w + 1)

    for v, w in items:
        # 重さを後ろから逆順にループする (同じ品物を2回使わないため)
        # range(start, stop, step) 
        for j in range(max_w, w - 1, -1):
            if dp[j - w] + v > dp[j]:
                dp[j] = dp[j - w] + v
            # (または Python らしく dp[j] = max(dp[j], dp[j - w] + v) と書いてもOK)

    print(dp[max_w])

if __name__ == '__main__':
    main()