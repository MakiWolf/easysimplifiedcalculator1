import calculation_class

number1 = 0
number2 = 0
result = 0
char = ""
exit = "0"
while exit == "0":
	number1 = input("number1: ")
	char = input("Enter (+, -, *, / OR : ")
	number2 = input("number2: ")
	
	if char == "+":
		print("result: ", calculation_class.add(number1, number2))	
	elif char == "-":
		print("result: ", calculation_class.sub(number1, number2))
	elif char == "*":
		print("result: ", calculation_class.mult(number1, number2))
	elif char == "/" or char == ":":
		print("result: ", calculation_class.div(number1, number2))
	else:
		print("unknown char")
	exit = "1"
	exit = input("Press 0 to continue calculating or 1 to exit.")
