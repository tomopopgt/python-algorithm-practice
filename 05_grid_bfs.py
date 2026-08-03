import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    h = int(input_data[0])
    w = int(input_data[1])
    sy = int(input_data[2])
    sx = int(input_data[3])
    gy = int(input_data[4])
    gx = int(input_data[5])

    # 残りのトークンからグリッド構造を構築
    rest = input_data[6:]
    grid = []

    if len(rest) == h * w:
        # スペース区切りの場合 (トークン数が H * W 個)
        for i in range(h):
            grid.append(rest[i * w : (i + 1) * w])
    else:
        # 行ごとの文字列の場合
        grid = rest[:h]

    # 距離配列の初期化 (-1 で未訪問を表現)
    dist = [[-1] * w for _ in range(h)]

    # キューの初期化 (Python 標準ライブラリ collections.deque)
    queue = deque([(sy, sx)])
    dist[sy][sx] = 0

    # 4方向（上下左右）の移動量
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # BFS (幅優先探索)
    while queue:
        cy, cx = queue.popleft()

        # ゴールに到達した場合
        if cy == gy and cx == gx:
            print(dist[cy][cx])
            return

        # 4方向へ移動を試みる
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            # グリッドの範囲内 かつ 壁でないか
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == '.':
                # 未訪問であれば訪問処理
                if dist[ny][nx] == -1:
                    dist[ny][nx] = dist[cy][cx] + 1
                    queue.append((ny, nx))

    # ゴールに辿り着けない場合
    print(-1)

if __name__ == '__main__':
    main()