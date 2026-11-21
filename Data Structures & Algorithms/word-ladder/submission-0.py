class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        N = len(wordList[0])
        adj = defaultdict(set)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                diffs = 0
                for k in range(N):
                    if wordList[i][k] != wordList[j][k]:
                        diffs += 1
                    if diffs > 1:
                        break
                if diffs == 1:
                    adj[wordList[i]].add(wordList[j])
                    adj[wordList[j]].add(wordList[i])
        
        q = deque([beginWord])
        visit = set([beginWord])
        transforms = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei == endWord:
                        return transforms + 1
                    if nei in visit:
                        continue
                    visit.add(nei)
                    q.append(nei)
            transforms += 1
        
        return 0
