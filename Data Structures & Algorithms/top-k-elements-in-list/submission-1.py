from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        freqs = [(freq, num) for num, freq in counts.items()]

        heapq.heapify_max(freqs)

        res = []
        while k > 0:
            freq, num = heapq.heappop_max(freqs)
            res.append(num)
            k -= 1
        
        return res
      