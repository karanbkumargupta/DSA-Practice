'''
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array.

Example2:
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array.
'''
from typing import List

# Time Complexity: O(N)
#
# Space Complexity: O(1)

arr = [2,5,1,3,0]


def find_largest(a:List[int]) -> int:
    largest = a[0]
    for i in range (1,len(a)):
        if a[i] > largest:
            largest = a[i]

    return largest

print(find_largest(arr))



#With Time Complexity: O(N*log(N))

# Space Complexity: O(1)

def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]

arr1 = [2, 5, 1, 3, 0]
arr2 = [8, 10, 5, 7, 9]
print("The Largest element in the array is:", sortArr(arr1))
print("The Largest element in the array is:", sortArr(arr2))

