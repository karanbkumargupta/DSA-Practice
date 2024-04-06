"""Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true"""

m = "paper"
n = "title"

mapping_s_t = {}
mapping_t_s = {}

def isomorphic_string(s,t):

    for i,j in zip(s,t):
        if i not in mapping_s_t:
            mapping_s_t[i]=j
        else:
            if mapping_s_t[i] != j:
                return False
        if j not in mapping_t_s:
            mapping_t_s[j]=i
        else:
            if mapping_t_s[j] != i:
                return False
    return True
print(isomorphic_string(m,n))
