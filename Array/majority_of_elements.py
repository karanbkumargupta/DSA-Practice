"""

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


# nums = [3,2,3]
nums = [2,2,1,1,1,2,2,6,6,6,6,2,2,2,2]

# def majority_of_element(nums):
#     count_el = {}
#
#     majo_length = len(nums)/2
#
#     print(majo_length)
#
#     for i in nums:
#         count_el[i] = count_el.get(i,0)+1
#
#         if count_el[i] > majo_length:
#             return i
#
# print(majority_of_element(nums))


#More's voting Algoritham

def majority_of_element(nums):

    count=0
    element = nums[0]
    for i in range(len(nums)):
        if nums[i] == element:
            count += 1
        else:
            count -= 1
        if count==0:
            element = nums[i]

    count=0
    for i in range(len(nums)):
        if nums[i] == element:
            count += 1
    if count<=len(nums)/2:
        return None
    else:
        return element



print(majority_of_element(nums))

