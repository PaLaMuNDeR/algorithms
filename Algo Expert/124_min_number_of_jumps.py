"""
Min Number Of Jumps
You are given a non-empty array of integers. Each element represents the maximum number of steps you can take forward.
For example, if the element at index 1 is 3, you can go from index Ito index 2, 3, or 4. Write a function that returns
the minimum number of jumps needed to reach the final index. Note that jumping from index i to index i + x always
constitutes 1 jump, no matter how large x is.
Sample input: [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3] Sample output: 4 (3 --> 4 or 2 --> 2 or 3 --> 7 --> 3)
"""

def minNumberOfJumps(array):
    if len(array)==1:
        return 0
    jump = 0
    steps = array[0]
    maxReach = array[0]
    for i in range(1,len(array)-1):
        maxReach = max(maxReach, array[i]+i)
        steps -= 1
        if steps == 0:
            jump += 1
            steps = maxReach-i

    return jump +1

print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
print(minNumberOfJumps([1]))
print(minNumberOfJumps([2,1,1]))
print(minNumberOfJumps([1,1,1]))