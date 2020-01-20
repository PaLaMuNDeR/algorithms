# Algorithms

# Coding Interview Bootcamp 
This is a repository with interesting interview questions and algorithms from the Udemy course
 [Coding Interview Bootcamp Algorithms and Data Structure](!https://www.udemy.com/course/coding-interview-bootcamp-algorithms-and-data-structure/) https://www.udemy.com/course/coding-interview-bootcamp-algorithms-and-data-structure/

While the course provides solutions in JavaScript - this repository presents them in Python.

## 02 - Reversed string

For a given string - print out the reversed the string
For example:
`reversed_string("abc") = "cba" `

## 03 - Fibonacci
Print the first n fibonacci numbers
A series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
The simplest is the series `1, 1, 2, 3, 5, 8, etc.`

## 04 - Palindrome
Given a string, return *True* if the string is palindrome
 or *False* if it is not. Palindromes are strings that
 form the same word if it is reversed. *Do* include spaces
 and punctuation in determining if the string is a palindrome.

```
 Examples:
     palindrome('abba') = True
     palindrome('abc')  = False
```

## 05 Reverse Integer

Given an integer return an integer that is the reverse

Examples:
reverseInt(15) -> 51
reverseInt(189) -> 981
reverseInt(500) -> 5
reverseInt(-15) -> -51
reverseInt(-90) -> -9

## 06 Max Char
Given a string, return the character that is most commonly used in the string.

```
Examples:

maxChar("abcccccccdef") -> "c"
maxChar("apple 12311111") -> "1"
```

## 07 FizzBuzz
Write a program that prints the numbers from 1 to n. But for multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

```
Example:
fizzbuzz(15)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

## 08 - Array chunk
Given an array and chunk size, divide the array into `chunk` amount of sub-arrays
 
 ```
 Examples:
 chunk([1,2,3,4],2) -> ([1,2],[3,4])
 chunk([1,2,3,4,5],2) -> ([1,2],[3,4],[5])
 chunk([1,2,3,4,5,6,7,8],3) -> ([1,2,3],[4,5,6],[7,8])
 chunk([1,2,3,4,5],4) -> ([1,2,3,4],[5])
 chunk([1,2,3,4,5],10) -> ([1,2,3,4,5])
 ```
 
 ## 09 - Anagrams
 Check to see if two provided strings are anagrams of each other.
One string is an anagram of another if it uses the same characters
in the same quantity. Only consider chars, not spaces or punctuation
Consider capital letters to be the same as lower case

```
 Examples:
     anagrams('rail safety', 'fairy tales') = True
     anagrams('RAIL! SAFETY!', 'fairy tales') = True
     anagrams('Hi there', 'Bye there') = False
```

## 10 - Capitalize Function
Write a function that accepts a string. The function should 
capitalize the first letter of each word in the string then 
return the capitalized string.

```
 Examples:
     capitalize('a short sentence') -> 'A Short Sentence'
     capitalize('a lazy fox') -> 'A Lazy Fox'
     capitalize('look, it is working!') -> 'Look, It Is Working!'
```

## 11 - Steps
 Write a function that should console log a step shape with N levels 
 using the # character. 
 Make sure the step has spaces on the right hand side.
```
 Examples:
 steps(2):
 '# '
 '##'
 steps(3):
 '#  '
 '## '
 '###'
 steps(4):
 '#   ' 
 '##  '
 '### '
 '####'
 ```
 
 ## 12 - Pyramid
 Write a function that accepts a positive number N.
 The function should console log a pyramid shape
 with N levels using the # character.  
 Make sure the step has spaces on the right and left hand side.

```
 Examples:
 pyramid(1):
 '#'
 pyramid(2):
 ' # '
 '###'
 steps(3):
 '  #  '
 ' ### '
 '#####'
 steps(4):
 '   #   ' 
 '  ###  '
 ' ##### '
 '#######'
 ```
 
## 13 - Vowels
Write a function that returns the number of vowels used in a
 string. Vowels are characters 'a', 'e', 'i', 'o', 'u'
 
 ```
 Examples:
 vowels('Hi There!') -> 3
 vowels('Why do you ask?') -> 4
 vowels('Why?') -> 0
```

## 14 - Matrix Spirals
Write a function that accepts an integer N and returns
 a NxN spiral matrix

```
 Examples:
 matrix(2)
  [[1,2],
   [3,4]]
   
 matrix(3)
  [[1,2,3],
   [8,9,4],
   [7,6,5]]
   
 matrix(4)
  [[ 1, 2, 3,4],
   [12,13,14,5],
   [11,16,15,6],
   [10, 9, 8,7]]
```

## 15 - Fibonacci Optimization
Optimize the Fibonacci solution with cache / memoization

## 16 - Linked List
Return the middle node of a Linked list.
If the list has an even number of elements, return the node
at the end of the first half of the list.
DO NOT use a counter variable, DO NOT retrieve the size of the list,
and only iterate through the list one time.

```
Example:
    const l = LinkedL()
    l.insertLast('a')
    l.insertLast('b')
    l.insertLast('c')
    midpoint(l) -> { data: 'b' }
```

## 17 - Weave Queue
"""
1. Implement - `peek` , `add` and `remove` functions to a Queue. `remove` should act as a `pop` and say what was the last element of the queue. `peek` should print out the last item of the queue without removing it.
2. Implement a `weave` function that merges two stacks into a third one with alternating content. The function should handle queues of different lengths. Only use `add`, `remove` and `queue`. Do not use the array
```
Example:
    QueueOne.add(1)
    QueueOne.add(2)
    QueueOne.add(3)
    QueueOne.add('hi')
    QueueOne.add('there)

    weave(QueueOne, QueueTwo)
    weave.remove() // 3
    weave.remove() // 'there'
    weave.remove() // 2
    weave.remove() // 'hi'
    weave.remove() // 1
```
    
## 18 - Trees
1. Create a `Node` class. The constructor should accept an argument that gets assigned to the data property and initialize
an empty array for storing children. The node class should have methods `add` and `remove`.
2. Create a `Tree` class. The tree constructor should initialize a `root` property to null.
3. Implement `traverseBF` and `traverseDF` that would get as an input a function and apply it to all the nodes in the tree

E.g.
```
                [20]
    [0]             [40]        [-15]
[-12] [-3] [1]                   [-2]
```

## 19 - Tree Width
Given the root node of a tree, return an array where each element is the width of tree at each level

Example:
```
Given:
    0
/   |   \
1   2   3
|       |
4       5

Answer: [1,3,2]
```

## 20 - Binary Search Trees
1. Implement the `Node` class to create a binary search tree. The constructor should initialize valuse `data`, `left`,
 and `right`

2. Implement the `insert` method for the Node class. Insert should accept an argument `data`, then create and insert a
 new node at the appropriate location in the tree.

3. Implement the `contains` method for the Node class. Contains should accept a `data` argument and return the Node in the tree with the same value.
If the value isn't in the tree return null.        

4. Validate the Binary Search Tree - given a node, validate the binary search tree, ensuring that every node's left hand
 child is less than the parent node's value, and that every node's right hand child is greater than the parent

## 21 - Sorting algorithms
Implement Bubble Sort, Selection Sort, Merge Sort

# Hacker Rank Challenges

## 22 Roads and Libraries
https://www.hackerrank.com/challenges/torque-and-development/problem
The Ruler of HackerLand believes that every citizen of the country should have access to a library. Unfortunately, HackerLand was hit by a tornado that destroyed all of its libraries and obstructed its roads! As you are the greatest programmer of HackerLand, the ruler wants your help to repair the roads and build some new libraries efficiently.

HackerLand has
cities numbered from to . The cities are connected by

bidirectional roads. A citizen has access to a library if:

    Their city contains a library.
    They can travel by road from their city to a city containing a library.

## 23 Chocolate distribution
Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her to make sure everyone gets the same number.

To make things difficult, she must equalize the number of chocolates in a series of operations. For each operation, she can give

chocolates to all but one colleague. Everyone who gets chocolate in a round receives the same number of pieces.

## 24 Max Subinterval
From an array select the best subinterval where the sum of its elements would be maximum.
The elements of the array could be negative.
-1,000,000<n<1,000,000

## 25 River size
River Sizes
You are given a two-dimensional array (matrix) of potentially unequal height and width
containing only Os and 1s. Each O represents land, and each 1 represents part of a river. A river
consists of any number of 1s that are either horizontally or vertically adjacent (but not
diagonally adjacent). The number of adjacent 1s forming a river determine its size. Write a
function that returns an array of the sizes of all rivers represented in the input matrix. Note that
these sizes do not need to be in any particular order.

## 26 Largest Range
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The first number in the output array should be the first number in the range while the second number should be the last number in the range. A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order to form a range. Assume that there will only be one largest range.
Sample input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] Sample output: [0, 7]

## 27 Max Profit With K Transactions 
You are given an array of integers representing the prices of a single stock on various days (each index in the array represents a different day). You are also given an integer k, which represents the number of transactions you are allowed to make. One transaction consists of buying the stock on a given day and selling it on another, later day. Write a function that returns the maximum profit that you can make buying and selling the stock, given k transactions. Note that you can only hold 1 share of the stock at a time; in other words, you cannot buy more than 1 share of the stock on any given day, and you cannot buy a share of the stock if you are still holding another share. 
Sample input: [5, 11, 3, 50, 60, 90], 2 Sample output: 93 (Buy: 5, Sell: 11; Buy: 3, Sell: 90) 

## 28 Cash register
Minimize the amount of coins you are returning to a client at a cash register. Assume you have coins of denomination: [25, 10, 5, 1]. 
How would you modify it, if you don't have the coins of 5 cents. 



# Algo Expert
Questions from https://algoexpert.com/ - use promo code `zweav-64` for 15% discount.


## Arrays

## 101 Two Number Sum
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order. If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.
Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 Sample output: [-1,11]

## 102 Three Number Sum 
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array. 
Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0 Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]] 

## 103 Smallest Difference 
Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers (one from the first array, one from the second array) whose absolute difference is closest to zero. The function should return an array containing these two numbers, with the number from the first array in the first position. Assume that there will only be one pair of numbers with the smallest difference. 
Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17] Sample output: [28, 26] 

## 104 Move Element To End 
You are given an array of integers and an integer. Write a function that moves all instances of that integer in the array to the end of the array. The function should perform this in place and does not need to maintain the order of the other integers. 
Sample input: [2, 1, 2, 2, 2, 3, 4, 2], 2 Sample output: [1, 3, 4, 2, 2, 2, 2, 2] (the numbers 1, 3, and 4 could be ordered differently) 

## 105 Four Number Sum 
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order. If no four numbers sum up to the target sum, the function should return an empty array. 
Sample input: [7, 6, 4, -1, 1, 2], 16 Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]] 

## 106 Subarray Sort 
Write a function that takes in an array of integers of length at least 2. The function should return an array of the starting and ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted. lithe input array is already sorted, the function should return [-1, -1]. 
Sample input: [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] Sample output: [3, 9] 

## 107 Min Rewards 
Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the final exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules: first, all students must receive at least one reward; second, any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score. Assume that all students have different scores; in other words, the scores are all unique. Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students, all the while satisfying the two rules. 
Sample input: [8, 4, 2, 1, 3, 6, 7, 9, 5] Sample output: 25 ([4, 3, 2, 1, 2, 3, 4, 5, 1]) 

## 108 - Zigzag Traverse 
Write a function that takes in a two-dimensional array and returns a one-dimensional array of all the array's elements in zigzag order. Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and proceeds in a zigzag pattern all the way to the bottom right corner. 
Sample input: [ 
[1, 3, 4,10], 
[2, 5, 9, 11], 
[6, 8, 12, 15], 
[7, 13, 14, 16], ] 
Sample output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] 


## 109 - Apartment Hunting 
You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your apartment, you want to optimize its location.You also have a list of requirements:a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment.The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question. For instance, for every block, you might know whether a school, a replan office, and a gym are present or not In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to reach all of your required buildings. Write a function that takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that is most optimal for you. 
Sample input: 
```
[{"gym": False, "school": True, "store": False,},
{"gym": True, "school": False, "store": False},
{"gym": True, "school": True, "store": False},
{"gym": False, "school": True, "store": False},
{"gym": False, "school": True, "store': True}],
["gym","school","store"]
```
Sample output: 3 (at index 3, the farthest you would have to walk to reach a gym, a school, or a store, is 1 block; at any other index,you would have to walk farther) 

## 110 - Calendar Matching 
Calendar Matching
Imagine that you want to schedule a meeting of a certain duration with a coworker. You have access to your calendar and your coworker's calendar (both of which contain your respective meetings for the day, in the form of [startTime, endTime]), as well as both of your daily bounds (i.e., the earliest and latest times at which you're available for meetings every day, in the form of [earliestTime, latestTime]). Write a function that takes in your calendar, your daily bounds, your coworker's calendar, your coworker's daily bounds, and the duration of the meeting that you want to schedule, and that returns a list of all the time blocks (in the form of [startTime, endTime]) during which you could schedule the meeting. Note that times will be given and should be returned in military time (example times: '8:30', '9:01', '23:56').
Sample input: 
```
['9:00', '10:30] , ['12:00', '13:00] , ['16:00', '18:00'],
['9:00', '20:00'],
['10:00', '11:30], ['12:30', '14:30], ['14:30', '15:00'], ['16:00', '17:00'],
['10:00', '18:30],
30 
```
Sample output: ['11:30', '12:00'] , ['15:00', '16:00'], ['18:00', '18:30']

## 111 - Caesar Cipher Encryptor 
Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the letter "a". 
Sample input: "xyz", 2 Sample output: "zab" 

## 112 - Longest Palindromic Substring 
Write a function that, given a string, returns its longest palindromic substring. A 
palindrome is defined as a string that is written the same forward and 
backward. Assume that there will only be one longest palindromic substring. 
Sample input: "abaxyzzyxf" 
Sample output: "xyzzyx" 

## 113 - Group Anagrams 
Write a function that takes in an array of strings and returns a list of groups of anagrams. Anagrams are strings made up of exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams. Note that the groups of anagrams don't need to be ordered in any particular way. 
Sample input: ["yo", "act", "flop", "tac", "cat", "oy", "olfp"] Sample output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]] 

## 114 - Longest Substring Without Duplication 
Write a function that takes in a string and that returns its longest substring without duplicate characters. Assume that there will only be one longest substring without duplication. 
Sample input: "clementisacap" Sample output: "mentisac" 

## 115 - Underscorify Substring 
Write a function that takes in two strings: a main string and a potential substring of the main string. The function should return a version of the main string with every instance of the substring in it wrapped between underscores. If two instances of the substring in the main string overlap each other or sit side by side, the underscores relevant to these two substrings should only appear on the far left of the left substring and on the far right of the right substring. If the main string does not contain the other string at all, return the main string intact. 
Sample input: "testthis is a testtest to see if testestest it works", "test" 
Sample output: " Jest_this is a _testtest_ to see if _testestest_ it works" 


## 116 - Find Closest Value In BST 
You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. You are also given a target integer value; write a function that finds the closest value to that target value contained in the BST. Assume that there will only be one closest value. 
Sample input: 10 ,12 / \ 5 15 / \ / \ 2 513 22 / \ 1 14 Sample output: 13 


## 117 - Same BSTs 
An array of integers is said to represent the Binary Search Tree (BST) obtained by inserting each integer in the array (from left to right) into the BST. Write a function that takes in two arrays of integers and returns a boolean representing whether or not these arrays represent the same BST. Note that you are not allowed to construct any BSTs in your code. A BST is a Binary Tree that consists only of BST nodes. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. 
Sample input: [10, 15, 8, 12, 94, 81, 5, 2, 11], [10, 8, 5, 15, 2, 12, 11, 94, 81] Sample output: True 


## 118 - Maximum Subset Sum With No Adjacent Elements 
Write a function that takes in an array of positive integers and returns an integer representing the maximum sum of non-adjacent elements in the array. If a sum cannot be generated, the function should return 0. 
Sample input: [75, 105, 120, 75, 90, 135] Sample output: 330 (75, 120, 135) 


## 119 - Number of ways to make a change
Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a function that returns the number of ways to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal. 
Sample input: 6, [1, 5] Sample output: 2 (1x1 + 1x5 and 6x1) 

## 120 - Min Number Of Coins For Change 
Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal. If it is impossible to make change for the target amount, return -1. 
Sample input: 7, [1, 5,10] Sample output: 3 (2x1 + 1x5) 

## 121 - Levenshtein Distance 
Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the first string to obtain the second string. There are three edit operations: insertion of a character, deletion of a character, and substitution of a character for another. 
Sample input: "abc", "yabd" Sample output: 2 (insert "y"; substitute "c" for "d") 

## 122 - Max Sum Increasing Subsequence 
Given an non-empty array of integers, write a function that returns an array of length 2. The first element in the output array should be an integer value representing the greatest sum that can be generated from a strictly-increasing subsequence in the array. The second element should be an array of the numbers in that subsequence. A subsequence is defined as a set of numbers that are not necessarily adjacent but that are in the same order as they appear in the array. Assume that there will only be one increasing subsequence with the greatest sum. 
Sample input: [10, 70, 20, 30, 50, 11, 30] Sample output: [110, [10, 20, 30, 50]] 

## 123 - Longest Common Subsequence 
Implement a function that returns the longest subsequence common to two given strings. A subsequence is defined as a group of characters that appear sequentially, with no importance given to their actual position in a string. In other words, characters do not need to appear consecutively in order to form a subsequence. Assume that there will only be one longest common subsequence. 
Sample input: "ZXVVYZW", "XKYKZPW" 

## 124 - Min Number Of Jumps 
You are given a non-empty array of integers. Each element represents the maximum number of steps you can take forward. For example, if the element at index 1 is 3, you can go from index Ito index 2, 3, or 4. Write a function that returns the minimum number of jumps needed to reach the final index. Note that jumping from index i to index i + x always constitutes 1 jump, no matter how large x is. 
Sample input: [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3] Sample output: 4 (3 --> 4 or 2 --> 2 or 3 --> 7 --> 3) 

## 125 - Knapsack Problem 
You are given an array of arrays. Each subarray in this array holds two integer values and represents an item; the first integer is the item's value, and the second integer is the item's weight. You are also given an integer representing the maximum capacity of a knapsack that you have. Your goal is to fit items in your knapsack, all the while maximizing their combined value. Note that the sum of the weights of the items that you pick cannot exceed the knapsack's capacity. Write a function that returns the maximized combined value of the items that you should pick, as well as an array of the indices of each item picked. Assume that there will only be one combination of items that maximizes the total value in the knapsack. 
Sample input: [[1, 2], [4, 3], [5, 6], [6, 7]],10 Sample output: [10, [1, 3]] 


## 126 - Max Profit With K Transactions 
You are given an array of integers representing the prices of a single stock on various days (each index in the array represents a different day). You are also given an integer k, which represents the number of transactions you are allowed to make. One transaction consists of buying the stock on a given day and selling it on another, later day. Write a function that returns the maximum profit that you can make buying and selling the stock, given k transactions. Note that you can only hold 1 share of the stock at a time; in other words, you cannot buy more than 1 share of the stock on any given day, and you cannot buy a share of the stock if you are still holding another share. Note that you also don't need to use all k transactions that you're allowed. 
Sample input: [5, 11, 3, 50, 60, 90], 2 Sample output: 93 (Buy: 5, Sell: 11; Buy: 3, Sell: 90) 

## 127 - Kadane's Algorithm 
Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing up all the numbers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers. 
Sample input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4] Sample output: 19 ([1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]) 
