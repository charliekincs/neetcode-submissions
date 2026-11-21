class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = {}
        for task in tasks:
            freqs[task] = 1 + freqs.get(task, 0)
        heap = [(freq, task) for task, freq in freqs.items()]
        heapq.heapify_max(heap)
        cycles = 0
        cooldown_q = deque()
        while heap or cooldown_q:
            if cooldown_q and cycles - cooldown_q[0][0] > n:
                c, t, f = cooldown_q.popleft()
                heapq.heappush_max(heap, (f - 1, t))

            if heap:
                freq, task = heapq.heappop_max(heap)
                if freq - 1 > 0:
                    cooldown_q.append((cycles, task, freq))

            cycles += 1

        return cycles
