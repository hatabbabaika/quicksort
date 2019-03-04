

def sort(list_, pivot=None, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(list_) - 1

    if end - start > 0:
        if pivot is None:
            pivot = __find_pivot__(list_, start, end)

        pivot_pos = __partition__(list_, pivot, start, end)
        sort(list_, None, start, pivot_pos - 1)
        sort(list_, None, pivot_pos + 1, end)


def __find_pivot__(list_, start, end):
    middle = (start + end) // 2
    if list_[middle] < list_[start]:
        __swap_items__(list_, start, middle)
    if list_[end] < list_[start]:
        __swap_items__(list_, start, end)
    if list_[end] < list_[middle]:
        __swap_items__(list_, end, middle)

    return list_[middle]


def __partition__(list_, pivot, start, end):
    while not start >= end:
        while list_[start] < pivot:
            start += 1

        while list_[end] > pivot:
            end -= 1

        __swap_items__(list_, start, end)

    return start


def __swap_items__(list_, i, j):
    list_[i], list_[j] = list_[j], list_[i]
