# #ordinary way
# list = [1,2,3,4,5,1,2,3,4,1,2,3,1,9]
# new_list = []

# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)



#genius way
original_list = [1, 2, 3, 4, 5, 1, 2, 3, 1, 9,2,3,4,5,2,7,8]
print(list(set(original_list)))
