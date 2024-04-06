"""Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()"."""

s = "(()())(())"
s = "(()())(())(()(()))"
s = "()()"

result = ""
count = 0
for char in s:
    if char == "(":
        if count > 0:
            result += char
        count += 1
    else:
        count -= 1
        if count > 0:
            result += char

print(result)