"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


For example, 2 is written as II in Roman numeral,
just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""


roman_dict={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}

# roman_dict_aux={"IV":4, "IX":9, "XL":40, "XC":90, "CD":90, "CM":900}


def roman_to_integer(roman_letter):
    Integer_sum=0

    for i in range(len(roman_letter)):

        if i > 0 and roman_dict[roman_letter[i]]> roman_dict[roman_letter[i-1]]:
            Integer_sum += roman_dict[roman_letter[i]] - (2*roman_dict[roman_letter[i-1]])
        else:
            Integer_sum += roman_dict[roman_letter[i]]

    return Integer_sum

print(roman_to_integer("MCMXCIV"))









