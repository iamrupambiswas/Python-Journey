n = int(input("Enter a number: "))
inputValue = n
sumOfPowers = 0
lenOfInput = len(str(n))
rem = 0

while n > 0:
    rem = n % 10
    sumOfPowers += rem ** lenOfInput
    n = n//10
print(f"{inputValue} is an armstrong number!" if inputValue == sumOfPowers else f"{inputValue} is not an armstrong number!")