"""
Longest Palindromic Substring
Write a function that, given a string, returns its longest palindromic substring. A
palindrome is defined as a string that is written the same forward and
backward. Assume that there will only be one longest palindromic substring.
Sample input: "abaxyzzyxf"
Sample output: "xyzzyx"

"""

def longestPalindromicSubstring(string):
    longestPalindrom = string[0]
    for i in range(1,len(string)):
        odd = checkPalindrom(string, i-1, i+1)
        even = checkPalindrom(string, i, i+1)
        if len(odd) > len(longestPalindrom):
            longestPalindrom = odd
        if len(even) > len(longestPalindrom):
            longestPalindrom = even
    return longestPalindrom


def checkPalindrom(string, indexLeft, indexRight):
    while indexLeft >=0 and indexRight < len(string):
        if string[indexLeft] != string[indexRight]:
            break
        else:
            indexLeft -= 1
            indexRight += 1

    return string[indexLeft+1:indexRight]


print(longestPalindromicSubstring('abaxyzzyxf'))
print(longestPalindromicSubstring('a'))