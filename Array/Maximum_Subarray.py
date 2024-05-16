"""

Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

nums = [5,4,-1,7,8]



#TC-O(N*2),SC-O(1)

def maxSubArray(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i,len(nums)):

            current_sum = current_sum + nums[j]

            max_sum=max(current_sum, max_sum)

    return max_sum


# print(maxSubArray(nums))



#Kadan's Algorithm

#O(N),O(1)

def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 0


    for i in range(len(nums)):


        if current_sum==0:
            start=i

        current_sum = current_sum + nums[i]

        if (current_sum>max_sum):

            ans_start=start
            ans_end = i


            max_sum=current_sum

        if current_sum<0:
            current_sum=0



    return max_sum,nums[ans_start:ans_end+1]


print(maxSubArray(nums))

