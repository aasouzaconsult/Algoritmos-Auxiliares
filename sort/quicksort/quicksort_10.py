# quicksort


def quicksort(array):
    """

    Quicksort chooses a pivot element and splits the remaining n-1 elements
    into 2 sublists. left sublist contains elements to the left of pivot in
    eventual position and right sublists contains elements to the right of
    pivot. Then we merge the sublists by placing pivot element in between. We
    recursively sort the elements until sublists has 0 elements.

    """
    return _quicksort(array, 0, len(array))


def _quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        _quicksort(array, low, pivot)
        _quicksort(array, pivot+1, high)
    return array


def partition(array, low, high):
    # init pivot
    # init first high index
    # iterate through low to high
    #   if current element less than pivot element
    #       swap current element and first high element
    #       increment first high index
    # swap pivot element and first high element
    # return first high index
    pivot = high - 1
    first_high = low
    for i in xrange(low, high):
        if array[i] < array[pivot]:
            array[i], array[first_high] = array[first_high], array[i]
            first_high += 1
    array[pivot], array[first_high] = array[first_high], array[pivot]
    return first_high
