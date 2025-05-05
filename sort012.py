def sort012(arr):
    map_sort = {0: 0, 1: 0, 2: 0}
    for x in arr:
        if x == 0:
            map_sort[0] += 1
        elif x == 1:
            map_sort[1] += 1
        else:
            map_sort[2] += 1
    result = []
    for x in range(0, 3):
        result.extend([x for _ in range(0, map_sort[x])])
    return result


array = [0, 1, 2, 0, 1, 2]
print(sort012(array))
