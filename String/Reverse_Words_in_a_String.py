"""Example 1:
Input: s=”this is an amazing program”
Output: “program amazing an is this”

Example 2:
Input: s=”This is decent”
Output: “decent is This"""

s = "this is an     amazing program"

words = s.split()
result = ' '.join(reversed(words))
# print(result)

result = ' '.join(words[::-1])
# print(result)


result=""
start=0
for i, char in enumerate(s):
    if char == ' ' or i==len(s)-1:
        print(i)
        if i != len(s) - 1:
            end = i
        else:
            end = i+1

        word = s[start:end]
        print(word)
        result=word+' '+result if result else word
        print(result)
        start=i+1



print(result)