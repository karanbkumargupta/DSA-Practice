"""Example 1:
Input: CAT, ACT
Output: true
Explanation: Since the count of every letter of both strings are equal.

Example 2:
Input: RULES, LESRT
Output: false
Explanation: Since the count of U and T  is not equal in both strings."""

s="CAT"
t="ACT"

#Sort and compare equal or not, 1st approach

s_dict={}
t_dict={}

def anagrams():

    if len(s)!=len(t):
        return False

    for i in s:
        s_dict[i]=s_dict.get(i,0)+1

    for i in t:
        t_dict[i]=t_dict.get(i,0)+1


    for j in s_dict:
        if j not in t_dict.keys() or s_dict[j]!=t_dict[j]:
            return False

    return True

print(anagrams())