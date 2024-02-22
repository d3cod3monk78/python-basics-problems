class Stack:

	def __init__(self):
		self.__stack_array = []
		self.__tos = -1

	def push(self, item: int):
		if(self.__tos >= 9):
			print('Stack is full')
		else:
			self.__stack_array.append(item)
			self.__tos += 1

	def pop(self)->int:
		if(self.__tos < 0):
			print('Stack is underflow')
			return 0
		else:
			self.__tos -= 1
			return self.__stack_array[self.__tos + 1]

if __name__ == '__main__':
	new_stack = Stack()

	for x in range(10):
		new_stack.push(x)

	for y in range(10):
		print(new_stack.pop())
