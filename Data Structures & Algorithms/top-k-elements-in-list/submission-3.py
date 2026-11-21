class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequenciesMap = {}
        for num in nums:
            frequenciesMap[num] = 1 + frequenciesMap.get(num, 0)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequenciesMap.items():
            buckets[freq].append(num)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            bucketLen = len(buckets[i])
            for num in buckets[i]:
                if k > 0:
                    res.append(num)
                    k -= 1
                else:
                    break

        return res