"""

Example 1:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.


Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.
Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].



"""


#brut force

"""
iterate and make 2 array pos nand neg array
result_array will be

arr[2*i]=pos[i] #even index
arr[2*i+1]=neg[i] #odd index

TC will be O(N+N/2) and SC O(N)

def rearrange_by_sign(A):
    # Define 2 lists, one for storing positive and other for negative elements of the array.
    pos = []
    neg = []
  
    # Segregate the array into positives and negatives.
    for i in range(len(A)):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
  
    # Positives on even indices, negatives on odd.
    for i in range(len(pos)):
        A[2 * i] = pos[i]
    for i in range(len(neg)):
        A[2 * i + 1] = neg[i]
  
    return A




"""

#O(N) and SC O(N)

# nums = [3,1,-2,-5,2,-4]

# nums = [-1,1]
#
# ans=[0]*len(nums)
# pos_index=0
# neg_index=1
#
# for i in range (len(nums)):
#     if nums[i]>0:
#         ans[pos_index]=nums[i]
#         pos_index+=2
#     else:
#         ans[neg_index] = nums[i]
#         neg_index += 2
#
#
# print(ans)







# Variety-2

# positive and negative elements (not necessarily equal).

"""

Example 1:

Input:
arr[] = {1,2,-4,-5,3,4}, N = 6
Output:
1 -4 2 -5 3 4

Explanation: 

Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.
Leftover positive elements are 3 and 4 which are then placed at the end of the array.

Example 2:
Input:
arr[] = {1,2,-3,-1,-2,-3}, N = 6
Output:
1 -3 2 -1 3 -2
Explanation: 

Positive elements = 1,2
Negative elements = -3,-1,-2,-4
To maintain relative ordering, 1 must occur before 2.
Also, -3 should come before -1, and -1 should come before -2.
After alternate ordering, -2 and -4 are left, which would be placed at the end of the ans array.

"""



nums = [1,2,-4,-5,3,4]

nums = [1,2,-3,-1,-2,-3]
def rearrange_by_sign(A):
    # Define 2 lists, one for storing positive and other for negative elements of the array.
    pos = []
    neg = []

    # Segregate the array into positives and negatives.
    for i in range(len(A)):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])

    if len(pos) < len(neg):
        # Positives on even indices, negatives on odd.
        for i in range(len(pos)):
            A[2 * i] = pos[i]
            A[2 * i + 1] = neg[i]

        # Fill the remaining negatives at the end of the array.
        extra_index=2*len(pos)
        for i in range(len(neg)-len(pos)):
            A[extra_index] = neg[len(pos)+i]
            extra_index += 1
    else:
        # Positives on even indices, negatives on odd.
        for i in range(len(neg)):
            A[2 * i] = pos[i]
            A[2 * i + 1] = neg[i]

        # Fill the remaining negatives at the end of the array.
        extra_index = 2 * len(neg)
        for i in range(len(pos) - len(neg)):
            A[extra_index] = pos[len(neg) + i]
            extra_index += 1


    return A

print(rearrange_by_sign(nums))

"""
Time Complexity: O(2*N) { The worst case complexity is O(2*N) which is a combination of O(N) of traversing the array to segregate into neg and pos array and O(N) for adding the elements alternatively to the main array}.

Explanation: The second O(N) is a combination of O(min(pos, neg)) + O(leftover elements). There can be two cases: when only positive or only negative elements are present, O(min(pos, neg)) + O(leftover) = O(0) + O(N), and when equal no. of positive and negative elements are present, O(min(pos, neg)) + O(leftover) = O(N/2) + O(0). So, from these two cases, we can say the worst-case time complexity is O(N) for the second part, and by adding the first part we get the total complexity of O(2*N).

Space Complexity:  O(N/2 + N/2) = O(N) { N/2 space required for each of the positive and negative element arrays, where N = size of the array A}.
"""




