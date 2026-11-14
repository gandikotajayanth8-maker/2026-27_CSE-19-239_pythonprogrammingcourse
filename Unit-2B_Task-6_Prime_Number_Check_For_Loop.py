num = int(input("Enter a number (1-100): "))
if num <= 1:
    print(f"{num} is NOT a prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break   
            
    if is_prime:
        print(f"{num} is a prime number.") 
    else:
        print(f"{num} is NOT a prime number.")
