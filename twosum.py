def twosum(num, target):
    for i in range(0, len(num)):
        for j in range(1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]


nums = [3,3]
target = 6
print(twosum(nums, target))
