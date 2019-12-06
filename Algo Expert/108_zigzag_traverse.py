"""
Zigzag Traverse
Write a function that takes in a two-dimensional array and returns a one-dimensional array of all the array's elements
in zigzag order. Zigzag order starts at the top left corner of the two-dimensional array, goes down by one element, and
proceeds in a zigzag pattern all the way to the bottom right corner.
Sample input: [
[1,  3,  4, 10],
[2,  5,  9, 11],
[6,  8, 12, 15],
[7, 13, 14, 16], ]

Sample output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

"""

# O(n) time | O(n) space
def zigzagTraverse(array):
    width = len(array[0]) - 1
    height = len(array) - 1
    answer = []
    row, col = 0,0
    goingDown = True

    while not isOutOfBounds(row, col, height, width):
        answer.append(array[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1

    return answer

def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width

# print(zigzagTraverse([
# [1, 3,  4, 10],
# [2, 5,  9, 11],
# [6, 8,  12,15],
# [7, 13, 14,16], ]))
print(zigzagTraverse([
[1,  3,  4, 10, 11, 20],
[2,  5,  9, 12, 19, 21],
[6,  8,  13,18, 22, 27],
[7,  14, 17,23, 26, 28],
[15, 16, 24,25, 29, 30],]))