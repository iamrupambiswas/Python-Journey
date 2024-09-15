# #ordinary way
# n = int(input("Enter a value : "))
# if n % 2 == 0:
#     print(f"{n} is an even number!")
# else:
#     print(f"{n} is an odd number!")

#----------------------------------------------------------------

#genius way
n = int(input("Enter a value : "))
print(f"{n} is an even number!" if n%2 == 0 else f"{n} is an odd number!")