n = int(input("Enter a number: "))
inputValue = n
rem = 0
rev = 0
while n > 0:
    rem = n % 10
    n = n // 10
    rev = rev * 10 + rem
print(f"{inputValue} is a palindrome number" if inputValue == rev else f"{inputValue} is not a palindrome number!")