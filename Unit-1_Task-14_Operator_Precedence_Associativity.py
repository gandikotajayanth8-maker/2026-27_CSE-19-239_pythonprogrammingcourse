# Multiplication happens before addition
result = 5 + 3 * 2
print(result) 
# Parentheses force addition to happen first
result_forced = (5 + 3) * 2
print(result_forced) 
# Same precedence: evaluated Left-to-Right
result = 100 - 50 + 20
print(result)
# Exponent operator evaluates Right-to-Left
result = 2 ** 3 ** 2
print(result)
