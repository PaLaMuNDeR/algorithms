"""
Levenshtein Distance
Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the first string to obtain the second string. There are three edit operations: insertion of a character, deletion of a character, and substitution of a character for another.
Sample input: "abc", "yabd" Sample output: 2 (insert "y"; substitute "c" for "d")

"""

def levenshteinDistance(str1, str2):
    E = [[s for s in range(len(str1)+1)] for s2 in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        E[i][0] = E[i-1][0] + 1

    for r in range(1, len(str2)+1):
        for c in range(1, len(str1)+1):
            if str1[c-1] == str2[r-1]:
                E[r][c] = E[r-1][c-1]
            else:
                E[r][c] = 1 + min(E[r][c-1], E[r-1][c], E[r-1][c-1])
    return E[-1][-1]

print(levenshteinDistance("abc","yabd"))


# O(nm) time | O(min(n,m) space
def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    big = str1 if len(str1) >= len(str2) else str2
    evenEdits = [x for x in range(len(small) + 1)]
    oddEdits = [None for x in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i
        for j in range(1, len(small) + 1):
            if big[i-1] == small[j-1]:
                currentEdits[j] = previousEdits[j-1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j-1], previousEdits[j], currentEdits[j-1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]

print(levenshteinDistance("abc","yabd"))
