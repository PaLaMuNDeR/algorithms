# Algorithms

This is a repository with interesting interview questions and algorithms from the Udemy course
 [Coding Interview Bootcamp Algorithms and Data Structure](!https://www.udemy.com/course/coding-interview-bootcamp-algorithms-and-data-structure/).

While the course provides solutions in JavaScript - this repository presents them in Python.

# 02 - Reversed string

For a given string - print out the reversed the string
For example:
`reversed_string("abc") = "cba" `

# 03 - Fibonacci
Print the first n fibonacci numbers
A series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
The simplest is the series `1, 1, 2, 3, 5, 8, etc.`

# 04 - Palindrome
Given a string, return *True* if the string is palindrome
 or *False* if it is not. Palindromes are strings that
 form the same word if it is reversed. *Do* include spaces
 and punctuation in determining if the string is a palindrome.

```
 Examples:
     palindrome('abba') = True
     palindrome('abc')  = False
```

# 05 Reverse Integer

Given an integer return an integer that is the reverse

Examples:
reverseInt(15) -> 51
reverseInt(189) -> 981
reverseInt(500) -> 5
reverseInt(-15) -> -51
reverseInt(-90) -> -9

# 06 Max Char
Given a string, return the character that is most commonly used in the string.

```
Examples:

maxChar("abcccccccdef") -> "c"
maxChar("apple 12311111") -> "1"
```

# 07 FizzBuzz
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

# 08 - Array chunk
Given an array and chunk size, divide the array into `chunk` amount of sub-arrays
 
 ```
 Examples:
 chunk([1,2,3,4],2) -> ([1,2],[3,4])
 chunk([1,2,3,4,5],2) -> ([1,2],[3,4],[5])
 chunk([1,2,3,4,5,6,7,8],3) -> ([1,2,3],[4,5,6],[7,8])
 chunk([1,2,3,4,5],4) -> ([1,2,3,4],[5])
 chunk([1,2,3,4,5],10) -> ([1,2,3,4,5])
 ```
 
 # 09 - Anagrams
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

# 10 - Capitalize Function
Write a function that accepts a string. The function should 
capitalize the first letter of each word in the string then 
return the capitalized string.

```
 Examples:
     capitalize('a short sentence') -> 'A Short Sentence'
     capitalize('a lazy fox') -> 'A Lazy Fox'
     capitalize('look, it is working!') -> 'Look, It Is Working!'
```

# 11 - Steps
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
 
 # 12 - Pyramid
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
 
# 13 - Vowels
Write a function that returns the number of vowels used in a
 string. Vowels are characters 'a', 'e', 'i', 'o', 'u'
 
 ```
 Examples:
 vowels('Hi There!') -> 3
 vowels('Why do you ask?') -> 4
 vowels('Why?') -> 0
```

# 14 - Matrix Spirals
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

# 15 - Fibonacci Optimization
Optimize the Fibonacci solution with cache / memoization

# 16 - Linked List
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
