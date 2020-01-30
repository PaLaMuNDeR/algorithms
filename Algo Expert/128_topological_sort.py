"""
Topological Sort
You are given a list of arbitrary jobs that need to be completed; these jobs are represented by integers. You are also given a list of dependencies. A dependency is represented as a pair of jobs where the first job is prerequisite of the second one. In other words, the second job depends on the first one; it can only be completed once the first job is completed. Write a function that takes in a list of jobs and a list of dependencies and returns a list containing a valid order in which the given jobs can be completed. If no such order exists, the function should return an empty list.
Sample input: [1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]] Sample output: [1, 4, 3, 2] or [4, 1, 3, 2]

"""


def topologicalSort(jobs, deps):
    if deps == []:
        return jobs
    priority = {}
    answer = []
    order = {}
    for i in jobs: # Create a priority array to track dependencies
        priority[i] = []
        order[i] = 0
    for pair in deps:
        first, second = pair
        priority[second].append(first)
        order[second] += 1 # Increase the order counter for the node
    print(priority)
    print(order)

    minval = min(order.values())
    key = min(order, key=order.get)

    # If minval is 0, we can just add those to the answer, those tasks are not dependent.
    # Then we pop them out of our dictionaries
    while minval == 0:
        answer.append(key)
        order.pop(key)
        priority.pop(key)
        minval = min(order.values())
        key = min(order, key=order.get)

    # We will increase the order for each task that is not ready to be executed yet, so
    # the max_order for each task should not be higher than this, otherwise we have a loop.
    # (The queue for this node which might be all the other nodes + the queue for another node, which might be similar)
    max_order = len(jobs)

    # This loop should not go more than twice across all the remaining nodes, so less than O(2j)
    while len(priority) > 0:
        found_dependency = False
        for node in priority[key]:
            if node in priority.keys():
                order[key] += 1
                found_dependency = True
                print(key, order)
                if order[key] > max_order:  # If we exceed max-order we can just deduce there is loop
                    print(key, [])
                    return []
        if not found_dependency:
            answer.append(key)
            priority.pop(key)
            order.pop(key)
        if len(order) > 0:
            key = min(order, key=order.get)

    print(answer)
    return answer


print(topologicalSort([1, 2, 3], [[1,2],[2,1]]))
print(topologicalSort([1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]))