"""
Longest Substring Without Duplication
Write a function that takes in a string and that returns its longest substring without duplicate characters.
Assume that there will only be one longest substring without duplication.
Sample input: "clementisacap" Sample output: "mentisac"

"""


def longestSubstringWithoutDuplication(string):
    """
    Store the visited letters in a dictionary. When we meet a repetitive letter,
    update the new occurence and trim the current string to start from whenever the previous letter was found.
    Check what is the longest string and save it for the output.
    """
    visited = {}
    final_output = output = ''
    i = 0
    while i < len(string):
        letter = string[i]
        if letter not in visited.keys():
            visited[letter] = i
            output = output + string[i]
            i += 1
            if len(final_output) < len(output):
                final_output = output
        else:
            if len(final_output) < len(output):
                final_output = output
            start = output.find(letter)
            output = output[start+1:]
            output = output + letter
            visited[letter] = i
            i += 1
        print(output)
    return final_output

print(longestSubstringWithoutDuplication('abcdeabcdefc'))

