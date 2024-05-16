"""Example 1:
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
"""

# arr = [2,3,5]
# arr = [2,3,5,1,9]
arr = [1, 2, 3, 1, 1, 1, 1]
# a = [-1, 1, 1 , 1]
# N = 3
N = 7
# s = 5
s=3
longest=0

# TC:O(N*N*N)
# SC:O(1)

def longest_subarray(input_arr,longest,s,N):

    for i in range(N):
        for j in range(i+1,N):
            sum=0
            for k in range(i,j+1):

                sum += input_arr[k]
            if sum==s:
                longest=max(longest , j-i+1)
    return longest

# print(longest_subarray(arr,longest,s,N))


# TC:O(N*N)

def longest_subarray(input_arr,longest,s,N):

    for i in range(N):
        sum = 0
        for j in range(i,N):
            sum += input_arr[j]
            if sum==s:
                longest=max(longest , j-i+1)
    return longest



# print(longest_subarray(arr,longest,s,N))

# TC:O(N)
# SC:O(N)

dict_={}

# arr = [2,3,5,6,1,9,12,4]
# s=10

def longest_subarray(input_arr,longest,s,N):
    sum=0
    for i in range(N):
        sum += input_arr[i]
        if sum==s:
            longest=max(longest,i+1)

        rem = sum - s

        if rem in dict_:
            length = i - dict_[rem]
            longest = max(longest, length)


        if sum not in dict_:
            dict_[sum]=i


    return longest

# print(longest_subarray(arr,longest,s,N))



# TC:O(2N)
def longest_subarray(input_arr,s,N):

    left, right = 0, 0  # 2 pointers

    sum= input_arr[0]

    longest = 0

    while right<N:#O(N)
        while left <=right and sum>s: #not running everytime so O(N) not O(N*N)
            sum -= input_arr[left]
            left+=1

        if sum==s:
            longest=max(longest,right-left+1)

        right+=1


        if right <N:
            sum += input_arr[right]

    return longest



print(longest_subarray(arr,s,N))







