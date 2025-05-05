def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    result = merge(left, right)
    return result



def merge(left, right):
    result = []
    # i is for left and j for right
    i = j = 0

    while len(right) > j and len(left) > i:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(right[j:])
    result.extend(left[i:])

    return result


arr = [4,3,1,7,12,5]
sorted_array = merge_sort(arr)
print(sorted_array)
