class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.lower, num)
        pop = heapq.heappop_max(self.lower)
        heapq.heappush(self.upper, pop)
        if len(self.upper) > len(self.lower) + 1:
            pop = heapq.heappop(self.upper)
            heapq.heappush_max(self.lower, pop)

    def findMedian(self) -> float:
        if len(self.upper) > len(self.lower):
            return self.upper[0]

        return (self.upper[0] + self.lower[0]) / 2

        
        