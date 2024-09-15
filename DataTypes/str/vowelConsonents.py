# #ordinary way
# str = input("Enter a string: ")
# vowelCount = 0
# ConsonantCount = 0

# vowels = "aeiouAEIOU"

# for i in str:
#     if i in vowels:
#         vowelCount += 1
#     else:
#         ConsonantCount += 1
# print(f"The number of vowels in {str} is {vowelCount} and the number of consonants is {ConsonantCount}")


#genius way
str = input("Enter a string: ")
vowelCount = 0
ConsonantCount = 0

for i in str:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowelCount += 1
    else:
        ConsonantCount += 1
print(f"The number of vowels in {str} is {vowelCount} and the number of consonants is {ConsonantCount}")
    