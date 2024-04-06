"""Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
"""

def largest_odd_number(s):
    num = int(s)

    larget_odd = -1

    if num%2==1:
        return num
    else:
        for digit in s:
            current_digit=int(digit)
            if current_digit %2==1 and current_digit > larget_odd:
                larget_odd=current_digit
        return larget_odd

print(largest_odd_number("35427"))
print(largest_odd_number("52"))


