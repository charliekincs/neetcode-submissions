class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        indegrees = {ch: 0 for word in words for ch in word}
        for i in range(len(words) - 1):
            mismatch = False
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    adj[words[i][j]].append(words[i + 1][j])
                    indegrees[words[i + 1][j]] += 1
                    mismatch = True
                    break
            if not mismatch and len(words[i]) > len(words[i + 1]):
                return ''

        q = deque([node for node, indeg in indegrees.items() if indeg == 0])

        s = []
        while q:
            cur = q.popleft()
            s.append(cur)
            print(cur)
            for nei in adj[cur]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
        
        return ''.join(s) if len(s) == len(indegrees) else ''