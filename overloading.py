from multipledispatch import dispatch

class Test:

	@dispatch()
	def m(self):
		print("No parameters")

	@dispatch(int)
	def m(self, a: int):
		print(f'a: {a}')

	@dispatch(int, int)
	def m(self, a: int, b: int):
		print(f'a: {a} & b: {b}')

	@dispatch(float)
	def m(self, a: float):
		print(f'a: {a}')

if __name__ == '__main__':
	test = Test()
	test.m()
	test.m(10)
	test.m(10, 20)