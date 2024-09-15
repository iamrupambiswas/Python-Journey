n = int(input("Enter a number: "))
rev = 0
rem = 0
while n > 0:
    rem = n % 10
    rev = 10 * rev + rem
    n = n//10
print(f"Reverse of {n} is {rev}")