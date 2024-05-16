"""Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 2,3,4,5,1
Explanation:
Since all the elements in array will be shifted
toward left by one so ‘2’ will now become the
first index and ‘1’ which was present at
first index will be shifted at last.


Example 2:
Input: N = 1, array[] = {3}
Output: 3
Explanation: Here only element is present and so
the element at first index will be shifted to
last index which is also by the way the first index."""


# Time Complexity: O(n), slicing takes o(n).

# Space Complexity: O(n) as extra space is used


arr = [1,2,3,4,5]
k=1
def rotate_by_1_arr(array_input,k):
    result = array_input[k:len(array_input)] + array_input[0:k]
    return result
print(rotate_by_1_arr(arr,k))





# Time Complexity: O(n), as we iterate through the array only once.
#
# Space Complexity: O(1) as no extra space is used

def solve(arr, n):
    temp = arr[0]  # storing the first element of the array in a variable
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp  # assign the value of the variable at the last index
    for i in range(n):
        print(arr[i], end=" ")

n = 5
arr = [1, 2, 3, 4, 5]
solve(arr, n)
