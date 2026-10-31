p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time period: "))
compound_interest=p*((1+r/100)**t)-p
print(f"The compound interest is: {compound_interest}")