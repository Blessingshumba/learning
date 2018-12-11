"""This is a scientific calculator...."""

num1 = float(input("Enter your first number. "))
num2 = float(input("Enter your second number. "))
operator = str(input("Please enter the operator. "))
result_add = num1 + num2
result_sub = num1 - num2
result_product = num1 * num2
results_division = num1 / num2

# add comment
if operator == "+":
    print(result_add)
    print("a")

elif operator == "-":
    print(result_sub)
    print("b")

elif operator == "*":
    print(result_product)
    print("c")

elif operator == "/":
    print(results_division)
    print("d")

else:
    print("The operator is invalid")
    print("e")
