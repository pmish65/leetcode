def quicksort(arr, low, high, k):
    if low < high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return
        else:
            quicksort(arr, low, pivot_index - 1, k)
            quicksort(arr, pivot_index+1, high, k)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for x in range(low, high):
        if arr[x] <= pivot:
            i += 1
            arr[x], arr[i] = arr[i], arr[x]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

array = [2,3,6,5,8,7,4,1,9]
quicksort(array, 0, len(array)-1, 5)
print(array)