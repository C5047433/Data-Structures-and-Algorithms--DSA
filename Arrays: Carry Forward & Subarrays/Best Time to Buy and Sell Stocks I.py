Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Return the maximum possible profit.


Problem Constraints
0 <= A.size() <= 700000
1 <= A[i] <= 10^7


Input Format
The first and the only argument is an array of integers, A.


Output Format
Return an integer, representing the maximum possible profit.


Example Input
Input 1:
A = [1, 2]
Input 2:
A = [1, 4, 5, 2, 4]


Example Output
Output 1:
1
Output 2:
4


Example Explanation
Explanation 1:
Buy the stock on day 0, and sell it on day 1.
Explanation 2:
Buy the stock on day 0, and sell it on day 2.



============================================
CODE:
============================================

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
    """
    Calculate the maximum profit that can be achieved by
    buying and selling stocks on different days.

    Args:
    A (list[int]): List of stock prices on consecutive days.

    Returns:
    int: Maximum profit achievable.
    """
    

    if not A:
       return 0
    
    min_price = A[0] #Intialize minimum value to A[0]
    max_profit = 0  #Initilaize max_profit to 0

    for price in A:
       min_price = min(min_price, price)  #iterate over all the values and check the minimum 
       max_profit = max(max_profit, price - min_price) # Difference over every value to get max profit
    
    return max_profit #return Max_profit
