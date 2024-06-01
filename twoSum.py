def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in hashmap:
            return [hashmap[compliment], i]
        hashmap[nums[i]] = i
    return []

arr = [2, 3, 5, 7, 9] 
target = 9

# compliment = target - nums[i] | 9 - 2 = 7

print(twoSum(arr, target)) # [2, 7]