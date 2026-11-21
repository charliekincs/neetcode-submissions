class MinStack:

    stack: List
    initial_min_val: int
    past_mins: List

    def __init__(self):
        self.stack = []
        self.initial_min_val = float('inf')
        self.past_mins = []
        

    def push(self, val: int) -> None:
        if val <= self.getMinOrInitial():
            self.past_mins.append(val)

        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack == []:
            return
        if self.top() == self.getMin():
            self.past_mins.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.past_mins[-1]

    def getMinOrInitial(self):
        if self.stack == []:
            return float('inf')

        return self.past_mins[-1]

        