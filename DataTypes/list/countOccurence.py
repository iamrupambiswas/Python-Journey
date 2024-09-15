#ordinary way
list = [1,2,3,4,5,6,7,8,9,2,4,2]
n = int(input("Enter the number: "))
count = 0
for i in list:
    if i == n:
        count += 1
print(f"The number of occurrences of the {n} is {count}")




#smart way (using 'count' function)
list = [1,2,3,4,5,6,7,8,9,2,4,2]
n = int(input("Enter the number: "))
print(f"The number of occurrences of the {n} is {list.count(n)}")