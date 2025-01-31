class MyStack:

    def _init_(self):
        self._queueA = []
        self._queueB = []
    
    def push(self, x: int) -> None:
        self._queueB.append(x)
        while self._queueA:
            self._queueB.append(self._queueA.pop(0))
        self._queueA, self._queueB = self._queueB, self._queueA 

    
    def pop(self) -> int:
        return self._queueA.pop(0)
    
    def top(self) -> int:
        return self._queueA[0]

    def empty(self) -> bool:
        return len(self._queueA) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()