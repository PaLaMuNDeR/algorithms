"""
Min Number Of Coins For Change
Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal. If it is impossible to make change for the target amount, return -1.
Sample input: 7, [1, 5,10] Sample output: 3 (2x1 + 1x5)

"""

def minNumberOfCoinsForChange(n, denoms):
    nums = [float("inf") for amount in range(0,n+1)]
    nums[0] = 0
    for amount in range(0, n+1):
        for denom in denoms:
            if denom <= amount:
                nums[amount] = min(nums[amount], 1+nums[amount-denom])
    if nums[-1] != float("inf"):
        return nums[-1]
    else:
        return -1

print(minNumberOfCoinsForChange(10,[1,2,3]))