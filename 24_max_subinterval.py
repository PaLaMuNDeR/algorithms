"""
From an array select the best subinterval where the sum of its elements would be maximum.
The elements of the array could be negative.
-1,000,000<n<1,000,000
"""

def max_subinterval(arr):
    """
    Keep local max and best interval. If we go negative - clean the current interval and start again.
    :param arr:
    :return:
    """
    local_max = -1000000
    current_interval = []
    best_interval = []
    best_max = local_max
    for i in arr:

        current_interval.append(i)
        print("Adding: {}".format(i))
        local_max = sum(current_interval)

        if local_max < 0:
            current_interval = []
            print("Cleaning...")
        elif local_max > best_max:
            print("better!")
            best_max = local_max
            best_interval = current_interval
            print("best: {}".format(best_interval))

    return best_max, best_interval[:-1]


print(max_subinterval([1, 2, -5, 6, -1, 4, -2, 3, -40, 5, -2, 3]))
