import sys

def is_possible(length, a, k):
    """
    長さ length の木材を k 本以上切り出せるか判定する関数
    """
    count = 0
    for x in a:
        count += x // length  # 切り捨て除算で切り出せる本数を加算
    return count >= k

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2 : 2 + n]]

    # めぐる式二分探索
    # ok: 確実に可能な境界（長さ 0 は常に可能）
    # ng: 確実に不可能な境界（最大長 + 1 は不可能）
    ok = 0
    ng = max(a) + 1

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_possible(mid, a, k):
            ok = mid  # 可能なら ok 側を広げる
        else:
            ng = mid  # 不可能なら ng 側を狭める

    print(ok)

if __name__ == '__main__':
    main()