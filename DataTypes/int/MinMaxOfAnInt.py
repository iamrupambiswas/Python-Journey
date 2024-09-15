n = int(input("Enter a number: "))
largest = 0
smallest = 9

while n > 0:
    x1 = n % 10
    largest = max(largest, x1)
    smallest = min(smallest, x1)
    n = n // 10
print(f"The largest digit is {largest} and the smallest digit is {smallest}")
    