class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.extend([beginWord])
        adj = defaultdict(set)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                diffs = 0
                for k in range(len(beginWord)):
                    if wordList[i][k] != wordList[j][k]:
                        diffs += 1
                    if diffs > 1:
                        break
                if diffs == 1:
                    adj[wordList[i]].add(wordList[j])
                    adj[wordList[j]].add(wordList[i])
        
        q = deque([beginWord])
        visited = set()
        cnt = 0
        while q:
            print(q)
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return cnt + 1

                visited.add(cur)
                for nei in adj[cur]:
                    if nei not in visited:
                        q.append(nei)
            if q:
                cnt += 1

        return 0