str = input("Enter the string: ")

for i in range(0, len(str)):
    if str[i] == str[-i-1]:
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")