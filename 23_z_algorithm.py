import sys

def z_algorithm(s):
    """
    Z-algorithm: 各 i について S と S[i:] の最長共通接頭辞 (LCP) の長さを O(|S|) で計算
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    
    # 過去に一致が判明している最右の区間 [l, r]
    l, r = 0, 0
    
    for i in range(1, n):
        # 現在地 i が過去の一致領域 r に含まれる場合、計算済みの結果を再利用
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        # 一致する限り伸ばす
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
            
        # 最右の一致区間 [l, r] を更新
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
            
    return z


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = input_data[0]
    z = z_algorithm(s)

    # 配列をスペース区切りで出力
    print(" ".join(map(str, z)))


if __name__ == '__main__':
    main()