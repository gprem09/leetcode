def reverseArr(arr):
    temp = 0
    l, r = 0, len(arr) - 1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
        
    return arr

arr = [1, 2, 3, 4, 5]
print(reverseArr(arr)) # [5, 4, 3, 2, 1]