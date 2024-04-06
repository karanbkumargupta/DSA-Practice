"""Example 1:
Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.

Example 2:
Input Format: N = 3, array[] = {1,3}
Result: 2
Explanation: In the given array, number 2 is missing. So, 2 is the answer."""

arr=[1,2,4,5]
N=5

# #TC-O(N)
# #SC-O(1)
# def find_missing(arr,N):
#     j=1
#     for i in range(len(arr)):
#         if j-arr[i] !=0:
#             return j
#         j+=1
#
# print(find_missing(arr,N))


#TC-O(N*N)
#SC-O(1)

def find_missing(arr,N):

    for j in range(1,N):
        flag = 0
        for i in range (len(arr)):
            print(j,i)
            if arr[i] == j:
                flag = 1
                break

        if flag==0:
            return j
    return -1

print(find_missing(arr,N))



