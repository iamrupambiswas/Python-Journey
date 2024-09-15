n1 = float(input("Enter the first value: "))
n2 = float(input("Enter the second value: "))

if n1 - n2 == 0:
    print("Both numbers are equal.")
elif n1 > n2:
    print(f"{n1} is greater than {n2}.")
else:
    print(f"{n2} is greater than {n1}.")