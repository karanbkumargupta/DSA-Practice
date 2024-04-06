"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
strs = ["flower","flow","flight"]

prefix = strs[0]

for string in strs[1:]:
    j=0
    while j<len(prefix) and j < len(string)  and prefix[j]==string[j] :
        j+=1

    prefix = prefix[:j]

print(prefix)