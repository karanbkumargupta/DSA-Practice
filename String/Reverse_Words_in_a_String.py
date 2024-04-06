"""

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

"""


input_str = "a good   example"


# s=input_str
# s_l=s.split()[::-1]
# ans_s=" ".join(s_l)
# print(ans_s)



def reverse_words(s):
    ans_str=""
    space_list = []
    s = s.strip()

    for i in range(len(s)):

        if s[i] == " ":
            space_list.append(i)
    print(space_list)

    start=0
    for j in (space_list):

        ans_str = s[start:j] + " " + ans_str

        start=j+1

    ans_str = s[start:len(s)] + " " + ans_str



    return ans_str

print(reverse_words(input_str))