"""Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1"""

from typing import List

a_array=[1,2,4,7,7,5]
def second_largest(arr: List[int]) -> int:

    if len(arr)<=1:
        return -1
    arr.sort()
    if arr[-1]==arr[-2]:
        return arr[-3]
    return arr[-2]


# print(second_largest(a_array))


def second_largest(arr: List[int]) -> int:
    second_large = arr[0]
    first_large = arr[1]
    for i in range(len(arr)):
        if arr[i]>= second_large and arr[i]>= first_large:
            first_large=arr[i]
        elif arr[i]>= second_large and arr[i]< first_large:
            second_large=arr[i]
    return second_large


print(second_largest(a_array))


def second_smallest(arr: List[int]) -> int:
    second_small = float('inf')
    first_small = float('inf')
    for i in range(len(arr)):
        if arr[i]<= second_small and arr[i]<= first_small:
            first_small=arr[i]
        elif arr[i]<= second_small and arr[i]> first_small:
            second_small=arr[i]
    return second_small
print(second_smallest(a_array))

