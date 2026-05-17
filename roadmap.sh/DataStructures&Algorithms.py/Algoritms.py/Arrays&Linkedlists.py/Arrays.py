# #Arrays
# arr = [10 , 20 , 30 , 40 ,50]

# print(arr[0]) # -> 10

# arr.append(60) # -> [10 , 20 , 30 , 40 ,50 , 60] add to end 60
# arr.insert(2, 99) # -> [10 , 20 , 99 , 30 , 40 , 50 , 60] add 99
# arr.pop(2) # -> [10 , 20 , 30 , 40 ,50 , 60] deleted 99

# print(arr) # print all arr


# def sum_evens(arr):
#     total = 0
#     for i in arr:
#         if i % 2 == 0:
#             total += i
#     return total

# arr = [1 , 2, 3, 4 ,5  ,6 ,7 ,8 ,9 , 0, 10 ,11, 12, 10 , 120 ,130]
# print(sum_evens(arr))



# def two_sum(arr, target):
#     left = 0 
#     right = len(arr) - 1 

#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target:
#             return [left , right]
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1
        

# print(two_sum([1, 2, 3, 4, 6], 10))

# def reverse_array(arr):
#     left = 0
#     right = len(arr) - 1

#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1

#     return arr

   


# print(reverse_array([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]


# видали всі дублікати з відсортованого списку
def remove_duplicates(arr):
    result = []
    
    for i in arr:
        if i not in result:
            result.append(i)
    
    return result

print(remove_duplicates([1, 1, 2, 2, 3, 4, 4, 5]))  
#
def remove_duplicates2(arr):
    left = 0 
    for right  in range(1 , len(arr)):
        if arr[right] != arr[left]:
            left += 1
            arr[left] = arr[right]
            
    return arr[:left + 1]
print(remove_duplicates2([1, 1, 2, 2, 3, 4, 4, 5]))
