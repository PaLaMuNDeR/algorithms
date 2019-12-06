"""
You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment
that you could move into. In order to pick your apartment, you want to optimize its location.
You also have a list of requirements:a list of buildings that are important to you.
For instance, you might value having a school and a gym near your apartment.
The list of blocks that you have contains information at every block about all of the buildings that are present and
absent at the block in question.

For instance, for every block, you might know whether a school, a pool, an office, and a gym are present or not.
In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to
reach all of your required buildings.

Write a function that takes in a list of blocks and a list of your required buildings and that returns the location
(the index) of the block that is most optimal for you.

Sample input:
[{"gym": False, "school": True, "store": False,},
{"gym": True, "school": False, "store": False},
{"gym": True, "school": True, "store": False},
{"gym.: False, "school": True, "store": False},
{"gym.: False, "school": True, "store': True}],
["gym","school","store"]

Sample output: 3 (at index 3, the farthest you would have to walk to reach a gym, a school, or a store, is 1 block; at any other index,you would have to walk farther)
"""
# Time O(B^2 * R) | Space(1)
def apartmentHunting(blocks, reqs):
    best_block = 0
    min_score = float("inf")

    for block in range(len(blocks)):
        current_score = 0
        for req in reqs:
            if blocks[block][req] == True:
                blocks[block][req] = 0
                # pass
            else:
                step = 0
                while blocks[block][req] == False:
                    step += 1
                    neighbour1 = block + step
                    neighbour2 = block - step
                    if neighbour1 < len(blocks):
                        if blocks[neighbour1][req] is True or blocks[neighbour1][req] is 0:
                            blocks[block][req] = step
                            # print("  B1: {}. Assigned {} with value {} because of neighbour {}".format(block,req,step,neighbour1))
                    if neighbour2 >= 0:
                        if blocks[neighbour2][req] is True or blocks[neighbour2][req] is 0:
                            blocks[block][req] = step
                            # print("  B2: {}. Assigned {} with value {} because of neighbour {}".format(block,req,step,neighbour2))

        score = max(blocks[block].values())
        # blocks[block]['score'] = score
        if score < min_score:
            min_score = score
            best_block = block
    # print blocks
    return best_block


# Time O(B * R) | Space(B * R)
"""
Compute a matrix for checking what is the distance for each building for each requirement.
e.g. [[1,0,0,1,2],...] - the first building has gym 1 block away, the second has 0 blocks away, the third 0, the forth 1, the fifth 2
to compute it - we go twice through all the blocks - forward - we check what was the value behind us
then backwards through the array - checking if the next value was also having a gym. We don't nest them, so that's O(BR) for all the requirements

Then we compute the score for each building as in the previous example 
"""
def apartmentHunting(blocks, reqs):
    best_block = 0
    min_score = float("inf")
    req_matrix = [[float("inf") for c in range(len(blocks))] for b in range(len(reqs))]
    for req in range(len(reqs)):
        # Populate the matrix by going forward
        for block in range(len(blocks)):
            if blocks[block][reqs[req]]:
                req_matrix[req][block] = 0
            else:
                if block > 0:
                    req_matrix[req][block] = req_matrix[req][block-1] + 1


        # Update the matrix by going backwards
        for block in range(len(blocks)-2, -1,-1):
            if blocks[block][reqs[req]]:
                pass
            # elif block == 0:
            #     req_matrix[req][block] = req_matrix[req][block+1] + 1
            else:
                req_matrix[req][block] = min(req_matrix[req][block], req_matrix[req][block+1] + 1)


    for block in range(len(blocks)):
        score_array = []
        for req in range(len(reqs)):
            score_array.append(req_matrix[req][block])

        score = max(score_array)
        if score < min_score:
            blocks[block]['score'] = score
            min_score = score
            best_block = block

    return best_block

print(apartmentHunting([
{"gym": False, "school": True, "store": False,},
{"gym": True, "school": False, "store": False},
{"gym": True, "school": True, "store": False},
{"gym": False, "school": True, "store": False},
{"gym": False, "school": True, "store": True}],
["gym","school","store"]))