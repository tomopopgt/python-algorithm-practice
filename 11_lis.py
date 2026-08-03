import sys
import bisect

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1 : 1 + n]]

    # dp[k] : 長さ k+1 の増加部分列における「末尾の要素の最小値」
    dp = []

    for x in a:
        # bisect_left で x 以上となる最初の位置を二分探索 (O(log N))
        idx = bisect.bisect_left(dp, x)

        if idx == len(dp):
            # x が既存のどの末尾よりも大きい場合、新しい長さの列を作る
            dp.append(x)
        else:
            # より小さな末尾の値に上書き更新する
            dp[idx] = x

    # dp 配列の長さがそのまま「最長増加部分列の長さ」となる
    print(len(dp))

if __name__ == '__main__':
    main()