num=int(input("Enter a number: "))
orig_num=num
work=num
sum=0
while work>0:
    digit=work%10
    sum=sum+digit
    work=work//10
    print(f"sum of digits of{orig_num} is {sum}")
    