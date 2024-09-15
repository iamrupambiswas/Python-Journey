list = [2,3,21,23,12,4,3,2,34,1]
largest = list[0]
smallest = list[0]

for i in list:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i
        
print(f"Largest: {largest}, Smallest: {smallest}")