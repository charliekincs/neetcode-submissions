class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        adj = defaultdict(set)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1:
                    adj[i].add(j)
                    adj[j].add(i)
        
        visit = set()
        def search(index):
            if index in visit:
                return
            
            visit.add(index)
            for nei in adj[index]:
                search(nei)

        search(0)
        return len(visit) == len(nums)
