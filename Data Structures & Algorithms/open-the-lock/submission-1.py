class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set()
        deadendsSet = set(deadends)

        q = deque(['0000'])
        count = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in deadendsSet or node in visit:
                    continue
                if node == target:
                    return count

                visit.add(node)
                for i in range(len(node)):
                    up   = str((int(node[i]) + 1) % 10)
                    down = str((int(node[i]) - 1) % 10)
                    nup = node[:i] + up + node[i+1:]
                    ndown = node[:i] + down + node[i+1:]
                    q.extend([nup,  ndown])
            count += 1
            
        return -1
