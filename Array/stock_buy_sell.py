"""

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and
sell on day 5 (price = 6), profit = 6-1 = 5.

Note: That buying on day 2 and selling on day 1
is not allowed because you must buy before
you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are
done and the max profit = 0.

"""

prices = [7,1,5,3,6,4]

# prices= [7,6,4,3,1]

max_profit = 0

# #O(N*2)
#
# for i in range(len(prices)):
#     for j in range(i+1,len(prices)):
#         profit = prices[j]-prices[i]
#
#         max_profit=max(profit,max_profit)
#
# print(max_profit)

# Time complexity: O(n)
#
# Space Complexity: O(1)

min_price=prices[0]
for i in range(1,len(prices)):
    min_price=min(prices[i],min_price)
    profit = prices[i] - min_price
    max_profit = max(profit, max_profit)
print(max_profit)

















