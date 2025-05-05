def reverseArray(arr):
    total_integer_in_arr = len(arr)
    number_of_iteration = int(total_integer_in_arr/2)
    for i in range(0, number_of_iteration):
        swap = arr[i]
        arr[i] = arr[total_integer_in_arr - i -1]
        arr[(total_integer_in_arr-i)-1 ] = swap
    return arr


arr1 = [1,2,3,4,5,6,7]
reverseArray(arr1)
print(arr1)
