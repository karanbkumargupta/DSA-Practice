"""

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

"""


#A-1 using two for loop


#A-2 prefix sum

nums = [3,1,2,4]
k=6

from collections import defaultdict
def subarraySum(arr,k):

    dict_pre=defaultdict(int)

    preSum=0

    count=0

    dict_pre[0]=1

    for i in range(len(arr)):
        preSum+=arr[i]
        rem=preSum-k
        count+=dict_pre[rem]
        dict_pre[preSum]+=1





    return count


print(subarraySum(nums,k))











