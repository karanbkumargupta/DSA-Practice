#right

"""Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , right
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position."""

# Time Complexity: O(n), slicing takes o(n).

# Space Complexity: O(n) as extra space is used


arr=[1,2,3,4,5,6,7]
arr=[3,7,8,9,10,11]
k=3




# def rotate_by_k_arr(array_input,k):
#     result = array_input[len(array_input)-k:len(array_input)] + array_input[0:len(array_input)-k]
#     return result
# print(rotate_by_k_arr(arr,k))

# or temp will take o(k) for (int i = n - k; i < n; i++)
#   {
#     temp[i - n + k] = arr[i];
#   }
#   for (int i = n - k - 1; i >= 0; i--)
#   {
#     arr[i + k] = arr[i];
#   }
#   for (int i = 0; i < k; i++)
#   {
#     arr[i] = temp[i];
#   }


#----------Approach-2 by reversing
# Time Complexity: O(n).

# Space Complexity: O(1)


# output
# 6 7 1 2 3 4 5

# reverse 0 to n-k
# 5 4 3 2 1
#reverse n-k to n
# 7 6
# reverse entire array
# 5432176

def reverse_array(arr_r,start,end):
    while start <= end :
        temp=arr_r[start]
        arr_r[start]=arr_r[end]
        arr_r[end]=temp
        start+=1
        end-=1
    return arr_r


def rotate_by_k_arr(array_input,k):
    n = len(array_input)

    print(reverse_array(array_input,0,n-k-1))
    print(reverse_array(array_input, n - k,n-1))
    print(reverse_array(array_input, 0, n-1))
    return array_input

print(rotate_by_k_arr(arr,k))


