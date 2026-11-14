# 1. Using break with a 'for' loop
 


n=int(input("Enter N (print until N,stop early at 5):"))
for number in range(1, n+1):
    if number == 5:
        print("Found 5! Stopping the loop.")
        break  # Exits the for loop immediately
    print("Current number:", number)

 

# 2. Using break with a 'while' loop
print("--- 2. While Loop Example ---")
n=int(input("Enter N (print until N,stop early at 5):"))
number = 1
while number <= n:
    if number == 5:
        print("Count reached 5! Stopping the loop.")
        break  # Exits the while loop immediately
    print("Current count:", number)
    number+= 1