def containsDuplicate(nums):
    # return true if arr contains duplicates
    # [1, 2, 3, 1] return True
    # [1, 2, 3, 4] return False

    map = {}

    for num in nums:
        if num in map:
            return True
        map[num] = 1
    return False

arr_1 = [1, 2, 3, 1]
arr_2 = [1, 2, 3, 4]

print(containsDuplicate(arr_1))
print(containsDuplicate(arr_2))