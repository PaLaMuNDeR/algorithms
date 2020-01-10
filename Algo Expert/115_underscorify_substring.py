"""
Underscorify Substring
Write a function that takes in two strings: a main string and a potential substring of the main string. The function should return a version of the main string with every instance of the substring in it wrapped between underscores. If two instances of the substring in the main string overlap each other or sit side by side, the underscores relevant to these two substrings should only appear on the far left of the left substring and on the far right of the right substring. If the main string does not contain the other string at all, return the main string intact.
Sample input: "testthis is a testtest to see if testestest it works", "test"
Sample output: "_test_this is a _testtest_ to see if _testestest_ it works"

"""

def underscorifySubstring(string, substring):
    """ We have to be careful where whe get repetitions of the same string"""
    locations = collapse(getLocations(string,substring))
    return underscorify(string,locations)

def getLocations(string,substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx+len(substring)])
            startIdx = nextIdx + 1
        else:
            break

    return locations

def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    previous = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            newLocations.append(current)
            previous = current
    return newLocations


def underscorify(string,locations):
    locationsIdx = 0
    stringIdx = 0
    inBetweenUnderscores = False
    finalChars = []
    i=0
    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]: #[[0,4],[8,12],[14,18]]
            finalChars.append('_')
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationsIdx += 1
            i = 0 if i == 1 else 1 #the start or the end of the substring
        finalChars.append(string[stringIdx])
        stringIdx += 1
    if locationsIdx < len(locations):
        finalChars.append("_")
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx:])
    return "".join(finalChars)