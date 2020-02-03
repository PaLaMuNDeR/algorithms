#!/bin/python
import os

"""
https://www.hackerrank.com/challenges/torque-and-development/problem
The Ruler of HackerLand believes that every citizen of the country should have access to a library. Unfortunately, HackerLand was hit by a tornado that destroyed all of its libraries and obstructed its roads! As you are the greatest programmer of HackerLand, the ruler wants your help to repair the roads and build some new libraries efficiently.

HackerLand has
cities numbered from to . The cities are connected by

bidirectional roads. A citizen has access to a library if:

    Their city contains a library.
    They can travel by road from their city to a city containing a library.

The following figure is a sample map of HackerLand where the dotted lines denote obstructed roads:

image

The cost of repairing any road is
dollars, and the cost to build a library in any city is dollars. If in the above example and , we would build roads at a cost of and libraries for a cost of . We don't need to rebuild one of the roads in the cycle

.

You are given
queries, where each query consists of a map of HackerLand and value of and

. For each query, find the minimum cost of making libraries accessible to all the citizens and print it on a new line.

Function Description

Complete the function roadsAndLibraries in the editor below. It must return the minimal cost of providing libraries to all, as an integer.

roadsAndLibraries has the following parameters:

    n: integer, the number of cities
    c_lib: integer, the cost to build a library
    c_road: integer, the cost to repair a road
    cities: 2D array of integers where each 

    contains two integers that represent cities connected by an obstructed road .

Input Format

The first line contains a single integer

, that denotes the number of queries.

The subsequent lines describe each query in the following format:
- The first line contains four space-separated integers that describe the respective values of
, , and , the number of cities, number of roads, cost of a library and cost of a road.
- Each of the next lines contains two space-separated integers, and , that describe a bidirectional road that connects cities and

.

Constraints

    Each road connects two distinct cities.

Output Format

For each query, print an integer that denotes the minimum cost to make libraries accessible to all the citizens on a new line.

Sample Input

2
3 3 2 1
1 2
3 1
2 3
6 6 2 5
1 3
3 4
2 4
1 2
2 3
5 6

Sample Output

4
12


"""

class City:
    """
        Parent of the city in a Graph
        Rank - how many sets have been connected to it
    """
    def __init__(self, parent, rank=0):
        self.parent = parent
        self.rank = rank


def MakeSet(x):
    """
        Transform a Node into a Set. It becomes its own parent with rank 0
    :param x: the Node(City)
    :return:
    """
    x.parent = x
    x.rank = 0


def FindRoot(x):
    """
        Find the Root (Parent) of a Node
    :param x: City
    :return:
    """
    if x.parent == x:
        return x
    else:
        return FindRoot(x.parent)


def Union(x,y):
    """
        Merge two sets into 1. It finds their roots and the one with the higher rank becomes parent. If the ranks are
        the same, then one becomes a parent, and the rank of the other raises - thus indicating the amount of its importance.
    :param x: City 1
    :param y: City 2
    :return:
    """
    xParent = FindRoot(x)
    yParent = FindRoot(y)

    if xParent.rank > yParent.rank:
        yParent.parent = xParent
    elif xParent.rank < yParent.rank:
        xParent.parent = yParent
    elif xParent != yParent:  # Merge them, cause they are not in the same set
        yParent.parent = xParent
        xParent.rank += 1


def roadsAndLibraries(n, c_lib, c_road, roads):
    """
        If the cost to build a library is less than a road - just build libraries.
        Otherwise:
            Use Kruskal Algorithm to connect the Cities to Graphs (increasing the `num_roads` used) and store them in `connected_components`.
            For each connected component we build 1 library.

        :param n: Amount of Cities
        :param c_lib: Cost of Library
        :param c_road: Cost of Road
        :param roads: Array of array of roads pairs between cities
        :return: Optimized cost
    """
    cities = []
    num_roads = 0

    if c_lib < c_road:
        return c_lib * n
    else:
        # Kruskal algorithm
        for i in xrange(n):
            cities.append(City(i))
            MakeSet(cities[-1])
        for (city1, city2) in roads:
            city1 = cities[city1 - 1]
            city2 = cities[city2 - 1]
            if FindRoot(city1) != FindRoot(city2):
                Union(city1, city2)
                num_roads += 1
        connected_components = set()
        for i in xrange(n):
            connected_components.add(FindRoot(cities[i]))
        return len(connected_components) * c_lib + num_roads * c_road


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        nmC_libC_road = raw_input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in xrange(m):
            cities.append(map(int, raw_input().rstrip().split()))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        # fptr.write(str(result) + '\n')
        print(str(result) + '\n')

    # fptr.close()
"""
2
3 3 2 1
1 2
3 1
2 3
6 6 2 5
1 3
3 4
2 4
1 2
2 3
5 6

1
5 3 6 1
1 2
1 3
1 4

5
9 2 91 84
8 2
2 9
5 9 92 23
2 1
5 3
5 1
3 4
3 1
5 4
4 1
5 2
4 2
8 3 10 55
6 4
3 2
7 1
1 0 5 3
2 0 102 1

"""