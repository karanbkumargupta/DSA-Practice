"""

You must return the length of the longest successive sequence.

Note:

You can reorder the array to form a sequence.
For example,

Input:
A = [5, 8, 3, 2, 1, 4], N = 6
Output:
5
Explanation:
The resultant sequence can be 1, 2, 3, 4, 5.
The length of the sequence is 5.

"""

A = [3, 4, 5]
N = 3
#
A = [100, 4, 200,1,3,2]
N = 6

# A = [5, 8, 3, 2, 1, 4]
# N = 6

# A = [1,2,2,1]
# N = 4


# N = 21
# A = [15, 6, 2, 1, 16, 4, 2, 29, 9, 12, 8, 5, 14, 21, 8, 12, 17, 16, 6, 26, 3]


# A = [1, 4,7, 3]
# N = 4

#------------------------------------
#TC:O(N*3)

def ls(arr,element):
    for i in arr:
        if i==element:
            return True
    return False


def longestSuccessiveElements(num, n):


    longest_su = 1

    for i in range(len(num)):
        x=num[i]
        count=1



        while (ls(num,x+1)==True):

            x=x+1
            count+=1

        longest_su=max(count,longest_su)

    return longest_su



# print(longestSuccessiveElements(A, N))


#------------------------------------

# TC:O(NlogN)+O(N)
def longestSuccessiveElements(num, n):

    last_smaller=float("-inf")
    longest_su = 1
    count=0

    num=sorted(num)

    for i in range(len(num)):
        if num[i]-1==last_smaller:
            count += 1
            last_smaller=num[i]
        elif num[i]!=last_smaller:
            count=1
            last_smaller = num[i]
        longest_su=max(longest_su,count)

    return longest_su



# print(longestSuccessiveElements(A, N))



#------------------------------------

# TC:#O(3N)

def longestSuccessiveElements(num, n):

    st = set(num)

    longest_su = 1
    for i in st:
        if i-1 not in st:
            count = 1
            x=i
            while x+1 in st:
                x+=1
                count+=1
            longest_su = max(longest_su, count)

    return longest_su

print(longestSuccessiveElements(A, N))

