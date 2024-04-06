'''
N = 5, array[] = {1,2,3,4,5}
N = 5, array[] = {5,4,6,7,8}
'''

#With Time Complexity: O(N*log(N))

# Space Complexity: O(1)


arr_1=[1,2,3,4,5]
arr_2=[5,4,6,7,8]
def check_arr(arra):
    backup_arr= arra
    if sorted(arra)==backup_arr:
        return True
    else:
        return False

print(check_arr(arr_1))
print(check_arr(arr_2))



# Time Complexity: O(N^2)
#
# Space Complexity: O(1)


def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return False

    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    ans = isSorted(arr, n)
    if ans:
        print("True")
    else:
        print("False")



# Time Complexity: O(N)
#
# Space Complexity: O(1)
def isSorted(arr, n):
    for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False

    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print("True" if isSorted(arr_2, n) else "False")

