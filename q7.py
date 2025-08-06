# def partition(arr):
#     n = len(arr)
#     print(n)
#     odd_index = 0  # Position where the next odd number should be placed

#     for i in range(n):
#         if arr[i] % 2 == 1:  # It's an odd number
#             odd_num = arr[i]
#             # Shift even numbers to the right
#             j = i
#             while j > odd_index:
#                 arr[j] = arr[j - 1]
#                 j -= 1
#             arr[odd_index] = odd_num
#             odd_index += 1

# # Test the function
# original_list = [10, 14, 15, 20, 13, 17, 40, 25, 30, 50]
# print("Original array:", original_list)

# partition(original_list)

# print("Modified array:", original_list)


def partition(arr):
    n = len(arr)
    idx = 0
    for i in range(n):
        if(arr[i]%2 == 1):
            num = arr[i]
            j  =i
            while(j>idx):
                arr[i] = arr[i-1]
                j = j-1
            arr[idx] = num
            idx += 1
original_list = [10, 14, 15, 20, 13, 17, 40, 25, 30, 50]
print("Original array:", original_list)

partition(original_list)

print("Modified array:", original_list)
