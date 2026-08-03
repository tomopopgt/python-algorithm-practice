import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    a = [int(x) for x in input_data[2 : 2 + n]]

    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    results = []
    idx = 2 + n
    for _ in range(q):
        left = int(input_data[idx])
        right = int(input_data[idx + 1])
        idx += 2
        results.append(str(s[right] - s[left]))

    print('\n'.join(results))

if __name__ == '__main__':
    main()