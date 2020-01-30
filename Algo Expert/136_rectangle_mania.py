"""
Rectangle Mania
Write a function that takes in a list of Cartesian coordinates (i.e., (x, y) coordinates) and returns the number of rectangles formed by these coordinates. Note that a rectangle must have four corners present in order to be counted, and we only care about rectangles with sides parallel to the x and y axes (i.e., with horizontal and vertical sides--no diagonal sides). You can also assume that no coordinate will be farther than 100 units from the origin.
Sample input: [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]] Sample output: 6

"""
def rectangleMania(array):
    """ Let's consider `pair` every potential lower-left corner of a square
    then look for upper-right and then the rest"""
    squares = 0
    for pair in range(0, len(array)):
        for second_pair in range(0, len(array)):
            if array[pair][0] < array[second_pair][0] and array[pair][1] < array[second_pair][1]:
                lower_right = [array[pair][0], array[second_pair][1]]
                upper_left = [array[second_pair][0], array[pair][1]]
                if upper_left in array and lower_right in array:
                    squares += 1
    return squares