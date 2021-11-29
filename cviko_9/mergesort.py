def merge(left, right):
    # not implemented
    pass


def mergesort(arr, start, end):
    if start == end - 1:
        return [arr[start]]

    middle = (start + end) // 2
    left_arr = mergesort(arr, start, middle)
    right_arr = mergesort(arr, middle, end)

    return merge(left_arr, right_arr)
