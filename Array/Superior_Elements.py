"""
An element is called a Superior Element if it is greater than all the elements present to its right.
The last element of the array is always a Superior Element.

Example

Input: a = [1, 2, 3, 2], n = 4

Output: 2 3

The final answer is in sorted order.

Sample Input 1:
4
1 2 2 1


Sample Output 1:
1 2


Sample Input 2:
3
5 4 3

Sample Output 2:
3 4 5

Try to solve this in O(n).

"""

a = [1, 2, 3, 2]
# a = [1, 2, 2, 1]
# a = [5, 4, 3]
n = 4

# time
# complexity
# of
# this
# function is O(n ^ 2)

def superiorElements(arr):
    result=[]
    n=len(arr)
    for i in range(len(arr)):
        flag=True
        for j in range (i+1,n):
            if a[i]<=a[j]:
                flag=False
        if flag:
            result.append(a[i])

    return result[::-1]



# print(superiorElements(a))


#approch 2
#greater then max(all element in right)


# a = [1,2,8,5, 7, 3]
# n = 6



def superiorElements(arr):
    maxi = a[n - 1]
    result=[a[len(arr)-1]]
    for i in range(len(arr)-2,0,-1):
        flag=True

        if a[i]<maxi:
            flag=False
        maxi=max(maxi,a[i])
        if flag:
            result.append(a[i])

    return result
#sort O(NlogN) so TC will be if sorted answer needed O(N)+O(NlogN)


print(superiorElements(a))












