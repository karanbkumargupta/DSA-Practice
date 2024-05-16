"""Example 1:

Input: prices = {1, 1, 0, 1, 1, 1}

Output: 3

Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

Input: prices = {1, 0, 1, 1, 0, 1}

Output: 2

Explanation: There are two consecutive 1's in the array. """

prices = [1, 1, 0, 1, 1, 1]
def consucative_array(arr):
    max_length = 0
    count_length = 0
    for i in range (len(arr)):
        if arr[i]==1:
            count_length+=1
        else:
            count_length = 0
        max_length = max(count_length,max_length)


    return max_length

print(consucative_array(prices))