import timeit
import operator
""" Given an array and chunk size, divide the array into many subarrays
 where each subarray is of length size
 
 Examples:
 chunk([1,2,3,4],2) -> ([1,2],[3,4])
 chunk([1,2,3,4,5],2) -> ([1,2],[3,4],[5])
 chunk([1,2,3,4,5,6,7,8],3) -> ([1,2,3],[4,5,6],[7,8])
 chunk([1,2,3,4,5],4) -> ([1,2,3,4],[5])
 chunk([1,2,3,4,5],10) -> ([1,2,3,4,5])
 """

def chunk(arr, chunk):
    """Time - 47 sec."""
    small_list = []
    answer = []
    for i in arr:
        if len(small_list) < chunk:
            small_list.append(i)
        else:
            answer.append(small_list)
            small_list=[]
            small_list.append(i)


    answer.append(small_list)

    return answer


def chunk_with_slice(arr, chunk):
    """Time - 16 sec"""
    answer = []
    index = 0

    while index < len(arr):
        answer.append(arr[index:index+chunk])
        index = index+chunk

    return answer


# print( chunk([1,2,3,4],2))
# print(chunk([1,2,3,4,5],2))
# print("This")
# print(chunk([1,2,3,4,5,6,7,8,9,10],3))
# print( chunk([1,2,3,4,5],4))
# print( chunk([1,2,3,4,5],10))


arr_input = '[1,2,3,4,5,6,7,8,9,10]' * 10
chunk_input = 3
print "Method 1 - Chunk standard"
print min(timeit.repeat(lambda: chunk(arr_input, chunk_input)))

print "Method 2 - Chunk with slice"
print min(timeit.repeat(lambda: chunk_with_slice(arr_input, chunk_input)))

