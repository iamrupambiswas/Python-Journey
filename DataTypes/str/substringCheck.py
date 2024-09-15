# #ordinary way
# MAIN_STRING = 'I am Rupam Biswas'

# str = input("Enter a string: ")

# if str in MAIN_STRING:
#     print(f"{str} is present in {MAIN_STRING}")
# else:
#     print(f"{str} is not present in {MAIN_STRING}")
        
        
        
#smart way
MAIN_STRING = 'I am Rupam Biswas'

str = input("Enter a string: ")

if MAIN_STRING.find(str) != -1:
    print(f"{str} is present in {MAIN_STRING}")
else:
    print(f"{str} is not present in {MAIN_STRING}")