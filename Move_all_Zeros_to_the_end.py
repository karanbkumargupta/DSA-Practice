"""Example 1:
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

Example 2:
Input: 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order"""


#########Approach-1

# TC-O(N)
# SC-O(N)
# a=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
# a=[1,2,0,1,0,4,0]

def move_zeros(arr):
    count=0
    b=[]
    for i in range (len(arr)):
        if arr[i]==0:
            count+=1
        else:
            b.append(arr[i])
    for i in range (count):
        b.append(0)
    return b
# print(move_zeros(a))

#########Approach-2

a=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

# TC-O(N)
# SC-O(1)

# i to iterate over all element
# j to iterate over only non zero element
def move_zeros(arr):
    j=0
    for i in range (len(arr)):
        print(a[i],a[j])
        if arr[i] != 0:
            arr[j],arr[i]=arr[i],arr[j]
            j=j+1
        print(arr)
    return arr

print(move_zeros(a))