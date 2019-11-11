"""
Implement Bubble Sort, Selection Sort, Merge Sort

"""


def bubble_sort(arr):
    """
    For each element:
        Check the largest element and bring it to the end.
        Check if the elements before that are sorted correctly, if not - swap them.
    :return:
    """
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j+1]:
                if arr[j] > arr[j+1]:
                    a = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = a

    return arr


def select_sort(arr):
    """
    For each element:
        Assign the first element as the smallest,
        go through the rest and check if there is a smaller element.
        If there is - swap them and increase i.
    :param arr:
    :return:
    """

    for i in range(0, len(arr)):
        min_index = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min_index:
                min_index = arr[j]
                b = arr[i]
                arr[i] = arr[j]
                arr[j] = b

    return arr


def merge_sort(arr):
    """
        Split the array into chunks of single element arrays and then pass them to the merge function.
    :param arr:
    :return:
    """

    def merge(arr1, arr2):
        """
            For two arrays that are sorted.
            Check the first element of each list - pop the smaller one to the result list
        :param arr1:
        :param arr2:
        :return:
        """
        answer = []
        while arr1 or arr2:
            if arr1 and arr2:
                if arr1[0] < arr2[0]:
                    answer.append(arr1[0])
                    arr1 = arr1[1:]
                else:
                    answer.append(arr2[0])
                    arr2 = arr2[1:]
            elif arr1:
                for elem in arr1:
                    answer.append(elem)
                return answer
            else:
                for elem in arr2:
                    answer.append(elem)
                return answer

        return answer

    mid = len(arr)/2
    half_1 = arr[:mid]
    half_2 = arr[mid:]

    if len(arr) > 2:
        return merge(merge_sort(half_1), merge_sort(half_2))
    elif len(arr) == 2:
        return merge(half_1, half_2)
    elif len(arr) == 1:
        return arr

    return merge(half_1, half_2)


l = [7, 10, 3, 2, 1, 6, 8, 5, 4, 9]
print(bubble_sort(l))
l = [7, 10, 3, 2, 1, 6, 8, 5, 4, 9]
print(select_sort(l))
l = [7, 10, 3, 2, 1, 6, 8, 5, 4, 9]
print(merge_sort(l))