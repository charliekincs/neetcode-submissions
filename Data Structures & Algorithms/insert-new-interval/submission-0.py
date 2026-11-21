class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        res = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][1] >= new_start and new_end >= intervals[i][0]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        
        res.append(newInterval)
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
