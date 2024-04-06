"""Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb" """

s = "babad"

# longest_palindrome={}


#TC:O(N*3)
#SC:O(N)

def find_longest_palindrome(input_str):
    max_length = 0
    start = 0


    for i in range(len(input_str)):
        for j in range(i+1,len(input_str)):

            res=input_str[i:j+1]
            if res==res[::-1]:
                # longest_palindrome[res]=len(res)
                max_length = max(max_length,len(res))
                start=i

    return start,max_length

    # for k,v in longest_palindrome.items():
    #     if v==max(longest_palindrome.values()):
    #         return k
    #     else:
    #         return ""


start,max_length=find_longest_palindrome(s)
print(s[start:start+max_length])


#TC:O(N*2)
#SC:O(1)

n=len(s)
start=0
max_length=1

def find_longest_palindrome(input_str):


    #s = "cbbd"

    for i in range(2,n):
        low = i-1  #1
        high= i+1  #3

        while(high<n and input_str[high]==input_str[i]):
            high+=1

        while (low >=0 and input_str[low] == input_str[i]):
            low -= 1

        while(low>0 and high<n and input_str[low] == input_str[high]):
            low-=1
            high+=1

        length=high-low-1
        if (max_length<length):
            max_length = length
            start=low+1



    return max_length

# print(find_longest_palindrome(s))
# print(s[start:start+max_length])










