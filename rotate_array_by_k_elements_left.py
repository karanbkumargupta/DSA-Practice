"""Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , left
Output: 3 4 5 6 7 1 2
Explanation: array is rotated to left by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left
Output: 9 10 11 3 7 8
Explanation: Array is rotated to left by 3 position."""


arr=[1,2,3,4,5,6,7]
arr=[3,7,8,9,10,11]
#
#
# 1 2 3 4 5 6 7
# 2 1 7 6 5 4 3

k=3

def reverse_array(arr_rev,start,end):
    while(start<=end):
        temp=arr_rev[start]
        arr_rev[start]=arr_rev[end]
        arr_rev[end]=temp

        start+=1
        end-=1
    return arr_rev

def roatate_by_left(input_a,k,n):
    print(input_a,k)
    print(reverse_array(input_a, 0, k-1))
    print(reverse_array(input_a, k, n-1))
    print(reverse_array(input_a, 0, n - 1))

    return input_a

print(roatate_by_left(arr,k,len(arr)))

