"""

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17


"""
input_string = "aabcb"


def beauty(s):
    n = len(s)
    freq = [0]*26
    ans = 0
    for i in range(n):
        freq = [0]*26
        max_freq = 0
        for j in range(i, n):
            k = ord(s[j])-ord('a')
            freq[k]+=1
            max_freq = max(max_freq, freq[k])
            ans += (j-i+1) - max_freq
    return ans

beauty(input_string)

