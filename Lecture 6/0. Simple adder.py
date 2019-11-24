print("I am a nice adder. Please input two numbers and I will sum them")
addend_1 = input("First number:")
addend_2 = input("Second number:")
if not addend_1.isdigit() or not addend_2.isdigit():
    print("Sorry: one of the inputs does not seem to be a valid integer number.")
else:
    result = int(addend_1) + int(addend_2)
    print("Result: {}".format(result))
