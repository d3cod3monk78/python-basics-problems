class Stack:
    def __init__(self):
        self._stack_array = []
        self._tos = -1

    def push(self, item):
        if len(self._stack_array) >= 10:
            print("Stack is full")
        else:
            self._stack_array.append(item)
            self._tos += 1

    def pop(self):
        if self._tos < 0:
            print("Stack is underflow")
            return 0
        else:
            item = self._stack_array.pop()
            self._tos -= 1
            return item

if __name__ == "__main__":
    stack = Stack()

    for i in range(10):
        stack.push(i)

    for i in range(10):
        print(stack.pop())