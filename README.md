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
