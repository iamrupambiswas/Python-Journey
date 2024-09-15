# #ordinary way
# n = int(input("Enter a number : "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(f"Factorial of {n} is {factorial}")

#----------------------------------------------------------------

# #genius way (using recursion)
def factorial(x):
    return 1 if x==0 else x*factorial(x-1)
n = int(input("Enter a number : "))
print(f"Factorial of {n} is {1 if n==0 else factorial(n)}")