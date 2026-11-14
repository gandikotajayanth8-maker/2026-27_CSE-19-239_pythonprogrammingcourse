 # 1. Using pass with a 'for' loop
print("--- 1. For Loop Example ---")
for number in range(1, 6):
    if number == 3:
        pass  # Placeholder: does nothing, execution continues normally
        print("Pass executed at 3, still inside the block!")
    print("Current number:", number)

print("\n")

# 2. Using pass with a 'while' loop
print("--- 2. While Loop Example ---")
count = 1
while count <= 5:
    if count == 4:
        pass  # Useful when you plan to add logic for 4 later
    else:
        print("Current count:", count)
    count += 1

