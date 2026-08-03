import sys

def main():
    # 1. 全入力を一括取得
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    s = int(input_data[1])
    a = [int(x) for x in input_data[2 : 2 + n]]

    # 2. しゃくとり法の実装
    left = 0
    current_sum = 0
    min_len = float('inf')  # Python で「無限大」を表す標準的な書き方

    # right ポインタを右に押し広げていく
    for right in range(n):
        current_sum += a[right]

        # 合計が s 以上である限り、left を縮めて最小長さを更新
        while current_sum >= s:
            min_len = min(min_len, right - left + 1)
            current_sum -= a[left]
            left += 1

    # 3. 結果の出力 (更新されなかった場合は 0)
    if min_len == float('inf'):
        print(0)
    else:
        print(min_len)

if __name__ == '__main__':
    main()