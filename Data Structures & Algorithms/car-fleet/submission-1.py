class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speeds = {}
        for i in range(len(position)):
            speeds[position[i]] = speed[i]
        
        position.sort(reverse=True)
        stack = []
        for pos in position:
            time = (target - pos) / speeds[pos]

            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)





