str = input("Enter a string: ")
reversed = ""

for i in str:
    reversed = i + reversed
print(reversed)