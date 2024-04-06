"""For example:

'str' = abcad and 'k' = 2.

We can see that the substrings {ab, bc, ca, ad} are the only substrings with 2 distinct characters.

Therefore, the answer will be 4.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
aacfssa
3
Sample Output 1 :
5
Explanation of The Sample Input 1:
Given 'str' = “aacfssa”. We can see that the substrings with only 3 distinct characters are {aacf, acf, cfs, cfss, fssa}.

Therefore, the answer will be 5.
Sample Input 2 :
qffds
4
Sample Output 2 :
1

"""

s = "qffds"
n = len(s)
k=4

count=0

for i in range (len(s)-k+1):
        res = s[i:k+i]


        if len(set(res))== k:
            count+=1
            continue

        j=0
        while(j<len(s)):

            res=res+s[len(res):len(res)+j+1]

            if len(set(res)) == k:
                count += 1
                break
            j=j+1



print(count)














