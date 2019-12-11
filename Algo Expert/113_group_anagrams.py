"""
Group Anagrams
Write a function that takes in an array of strings and returns a list of groups of anagrams.
Anagrams are strings made up of exactly the same letters, where order doesn't matter.
For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.
Note that the groups of anagrams don't need to be ordered in any particular way.

Sample input: ["yo", "act", "flop", "tac", "cat", "oy", "olfp"] Sample output: [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"]]

"""

def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord not in anagrams.keys():
            anagrams[sortedWord] = [word]
        else:
            anagrams[sortedWord] = anagrams[sortedWord]+[word]
    return list(anagrams.values())

print groupAnagrams(["yo", "act", "flop", "tac", "cat", "oy", "olfp"] )
