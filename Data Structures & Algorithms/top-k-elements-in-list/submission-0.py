from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums: 
            frequencies[num] = 1 + frequencies.get(num, 0)

        heap = [(-frequency, num) for num, frequency in frequencies.items()]

        heapq.heapify(heap)

        res = []
        while k > 0:
            neg_freq, num = heapq.heappop(heap)
            res.append(num)
            k -= 1

        return res