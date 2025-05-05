def maximum_minium(arr):
    maximum = 0
    minimum = 100001

    for x in arr:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x

    return minimum, maximum



input_arr = [56789]
print(maximum_minium(input_arr))