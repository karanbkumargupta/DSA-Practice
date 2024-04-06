"""Example 1:

Input: arr[1,1,2,2,2,3,3]

Output: arr[1,2,3,_,_,_,_]

Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Example 2:

Input: arr[1,1,1,2,2,3,3,3,3,4,4]

Output: arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array."""

#Apparch------11111

input_arr=[1,1,2,2,2,3,3]
# dict_op={}
# for i in range (len(input_arr)):
#     dict_op[input_arr[i]] = i
# print(dict_op.keys())
#

# Time complexity: O(n*log(n))+O(n)
#
# Space Complexity: O(n)

# set_op=set()
# for i in range (len(input_arr)):
#     set_op.add(input_arr[i])
# print(set_op)
#
# j=0
# for x in set_op:
#     input_arr[j]=x
#     j+=1
# for i in range(len(set_op)):
#         print(input_arr[i], end=" ")
# print(input_arr)




#Apparch 2

# Time Complexity: O(N)
#
# Space Complexity: O(1)

input_arr=[1,1,2,2,2,3,3]
from typing import List

def removeDuplicates(arr: List[int]) -> int:
    j=0
    for i in range (1,len(input_arr)):
        if input_arr[i]!=input_arr[j]:
            j += 1
            input_arr[j]=input_arr[i]
    return j+1


print(input_arr)
k = removeDuplicates(input_arr)
print("The array after removing duplicate elements is ")
for i in range(k):
    print(input_arr[i], end=" ")



    # remove duplicates and move all zero two pointer array check properly