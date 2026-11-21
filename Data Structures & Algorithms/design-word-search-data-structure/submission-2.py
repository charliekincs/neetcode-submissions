class TrieNode:
    def __init__(self):
        self.children = {}
        self.isCompleteWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            cur = cur.children[word[i]]
        cur.isCompleteWord = True

    def search(self, word: str) -> bool:

        def dfs(i, cur):
            if i == len(word):
                return cur.isCompleteWord
            if len(cur.children) == 0:
                return False
            if word[i] != '.':
                return dfs(i + 1, cur.children[word[i]]) if word[i] in cur.children else False

            for child in cur.children.values():
                if dfs(i + 1, child):
                    return True
            return False

        return dfs(0, self.root)
