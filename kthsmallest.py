def insertionsort(arr):
    arr_len = len(arr)
    for x in range(1, arr_len):
        for y in range(0, x):
            if arr[x] < arr[y]:
                swap = arr[x]
                arr[x] = arr[y]
                arr[y] = swap


def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high)

        # Sort the left part
        quick_sort(arr, low, pivot_index - 1)

        # Sort the right part
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]  # pivot is the last element
    i = low - 1  # place for the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot
    return i + 1



## def kthsmallest(arr, k):
arr = [8,4,5,3,1,4]
insertionsort(arr)
print(arr)
