"""

Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.

Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.

"""


"""
Time Complexity: O(N*logM) + O(M), where M = size of the map i.e. M = (N/2)+1. N = size of the array.
Reason: We are inserting N elements in the map data structure and insertion takes logM time(where M = size of the map). So this results in the first term O(N*logM). The second term is to iterate the map and search the single element. In Java, HashMap generally takes O(1) time complexity for insertion and search. In that case, the time complexity will be O(N) + O(M).

Note: The time complexity will be changed depending on which map data structure we are using. If we use unordered_map in C++, the time complexity will be O(N) for the best and average case instead of O(N*logM). But in the worst case(which rarely happens), it will be nearly O(N2).

Space Complexity: O(M) as we are using a map data structure. Here M = size of the map i.e. M = (N/2)+1.
"""

def find_element(input):
    count=1
    dict_={}

    # for num in input:
    #     dict_[num] = dict_.get(num, 0) + 1

    for i in range (len(input)):
        if input[i] not in dict_:
            dict_[input[i]]=count
        else:
            dict_[input[i]]=dict_[input[i]]+1
        print(dict_)


    for i,v in dict_.items():
        if v==1:
            return i

arr=[2,2,1]
# print(find_element(arr))


# try 2 for loop also



"""Assume the given array is: [4,1,2,1,2]
XOR of all elements = 4^1^2^1^2
      = 4 ^ (1^1) ^ (2^2)
      = 4 ^ 0 ^ 0 = 4^0 = 4
Hence, 4 is the single element in the array."""



def get_element(input_arr):
    xorr=0

    for i in range(len(input_arr)):
        xorr=xorr^input_arr[i]

    return xorr

print(get_element([4,1,2,1,2]))

"""
Time Complexity: O(N), where N = size of the array.
Reason: We are iterating the array only once.

Space Complexity: O(1) as we are not using any extra space."""
