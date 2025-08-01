import ast



print("------------ eval() function no upyog----------")


math_expression_string = "15 + (4 * 5) - 2"
print(f"\n1. Evaluating a math string: '{math_expression_string}'")

result = eval(math_expression_string)

print(f"   Result: {result}")
print(f"   Type of result: {type(result)}") # The result is a number, not a string
print("-" * 40)
