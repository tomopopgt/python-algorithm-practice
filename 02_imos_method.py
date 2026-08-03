import sys

def main():
    # 1. 全入力を一括取得
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    # 2. データの読み込みと最大時刻(max_time)の探索
    events = []
    max_time = 0
    idx = 1
    for _ in range(n):
        l = int(input_data[idx])
        r = int(input_data[idx+1])
        events.append((l, r))
        if r > max_time:
            max_time = r
        idx += 2

    # 3. いもす法用配列の初期化 (必要な長さだけ確保)
    # Python では [初期値] * 長さ で簡単に配列を作成できます
    imos = [0] * (max_time + 2)

    # 4. 区間の開始(+1)・終了(-1)を記録
    for l, r in events:
        imos[l] += 1
        imos[r] -= 1

    # 5. 累積和の計算 (配列を直接上書き更新していく)
    for i in range(1, max_time + 1):
        imos[i] += imos[i - 1]

    # 6. Python の組み込み関数 max() で配列内の最大値を一発取得！
    print(max(imos))

if __name__ == '__main__':
    main()