import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])
    b = int(input_data[2])

    # scores[i][j] : ステップ i で選択肢 j を選んだ際の加算スコア
    scores = []
    idx = 3
    for _ in range(n):
        row = [int(input_data[idx + j]) for j in range(m)]
        scores.append(row)
        idx += m

    # ビームサーチの初期状態: (累積スコア, 状態識別用データ)
    # 初期状態はスコア 0 の状態 1 つのみ
    current_beam = [0]

    for i in range(n):
        next_candidates = []
        # 現在保持している上位 B 個の状態それぞれから、次の M 個の選択肢を展開
        for current_score in current_beam:
            for choice_score in scores[i]:
                next_candidates.append(current_score + choice_score)

        # スコアが高い順にソートして、上位 B 個のみを残す (ビーム幅に絞り込み)
        next_candidates.sort(reverse=True)
        current_beam = next_candidates[:b]

    # 最終ステップのビーム内での最大スコアを出力
    print(max(current_beam))


if __name__ == '__main__':
    main()