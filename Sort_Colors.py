"""


Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

"""



nums = [2,0,2,1,1,0,0,1,2]
# nums = [2,0,1]

# def sort_color(nums_array):
#     color_dict = {}
#     for i in nums_array:  #O(N)
#         color_dict[i] = color_dict.get(i , 0)+1
#
#     return sorted([key for key,value in color_dict.items() for _ in range(value)]) #O(n log n).#
#
#
# print(sort_color(nums))

#2nd apprach merge sort so tc will be O(nlogn) and sc will be O(N)
#3rd approch iterate through the array count_0,count_1 and count_2 and fill the same array with 0,1,2 based on count #2N tc nd 1 sc


#dutch national flag Algo

# O(N) and O(1)

def sort_color(nums_array):

    low=0
    mid=0
    high=len(nums_array)-1


    while(mid<=high):

        if nums_array[mid]==0:

            temp=nums_array[mid]
            nums_array[mid]=nums_array[low]
            nums_array[low]=temp

            low=low+1
            mid=mid+1

        elif nums_array[mid]==1:
            mid=mid+1

        else:

            temp=nums_array[mid]
            nums_array[mid]=nums_array[high]
            nums_array[high]=temp

            high=high-1

    return nums_array




print(sort_color(nums))


