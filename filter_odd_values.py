def remove_odd_numbers(number_array):
	return [number for number in number_array if number % 2 == 0]


for number in remove_odd_numbers([int(x) for x in input("Enter the numbers that you need to filter seperated by a space").split()]):
	print(number)
