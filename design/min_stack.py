class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        return self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

    # check
    def getAll(self) -> int:
        return self.stack

obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
print('push', obj.getAll())

print('pop', obj.pop())
print('pop-all', obj.getAll())

print('top', obj.top())
print('top-all', obj.getAll())

print('getMin', obj.getMin())
print('getMin-all', obj.getAll())