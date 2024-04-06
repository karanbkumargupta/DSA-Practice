"""

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


# arr_input = [2,7,11,15]
arr_input = [3, 3]
target = 6

# if consucative postion sum is target

# def two_sum(arr_input):
#
#     for i in range(len(arr_input)-1):
#         if arr_input[i]+arr_input[i+1]==target:
#             return i,i+1
#
# print(two_sum(arr_input))


# If array is sorted

def two_sum(arr_input, target):
    left = 0
    right = len(arr_input) - 1

    while left < right:
        cur_sum = arr_input[left] + arr_input[right]

        if cur_sum == target:
            return left, right
        elif target > cur_sum:
            left = left + 1
        else:
            right = right - 1

    return -1


print(two_sum(arr_input, target))



#work for every possibilities using dict

#TC:O(N),SC:O(N)

# arr_input = [3, 2, 4, 1]
# target = 6
#
# num_dict={}
#
# def two_sum(arr_input, target):
#     for i,num in enumerate(arr_input):
#
#         subtract = target - num
#         if subtract in num_dict:
#             return [num_dict[subtract],i]
#
#         num_dict[num] = i
#
#     return -1
#
# print(two_sum(arr_input, target))
