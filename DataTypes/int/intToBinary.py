n = int(input("Enter a number: "))
binary = ''
while n>0:
    binary = str(n%2) + binary
    n = n//2
print(f"Binary of {n} is {binary}")