a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
rem = 1
gcd = 0
while(rem != 0):
    rem = a % b
    if(rem == 0):
        gcd = b
    else:
        a = b
        b = rem
print(f"GCD is {gcd}")