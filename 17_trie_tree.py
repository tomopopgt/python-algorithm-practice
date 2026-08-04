import sys

class TrieNode:
    """
    トライ木のノード構造体
    """
    def __init__(self):
        # 子ノードを辞書 (dict) で管理
        self.children = {}
        # このノードを通った単語の数
        self.count = 0


class Trie:
    """
    トライ木クラス
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        単語をトライ木に追加 (O(|word|))
        """
        node = self.root
        node.count += 1
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def count_prefix(self, prefix):
        """
        prefix で始まる単語の数を取得 (O(|prefix|))
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    trie = Trie()
    idx = 2

    # 1. 辞書単語の追加
    for _ in range(n):
        trie.insert(input_data[idx])
        idx += 1

    # 2. クエリ処理
    results = []
    for _ in range(q):
        prefix = input_data[idx]
        idx += 1
        results.append(str(trie.count_prefix(prefix)))

    print('\n'.join(results))


if __name__ == '__main__':
    main()