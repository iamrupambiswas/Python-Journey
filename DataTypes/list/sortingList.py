# #ordinary way
# list = [12,21,23,1,23,21,2,4,3]
# print(sorted(list, reverse=True))



# #bubble sort
# def bubble_sort(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
# my_list = [12, 21, 23, 1, 23, 21, 2, 4, 3]
# bubble_sort(my_list)
# print(my_list)



#insertion sort
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
my_list = [12, 21, 23, 1, 23, 21, 2, 4, 3]
insertion_sort(my_list)
print(my_list)

