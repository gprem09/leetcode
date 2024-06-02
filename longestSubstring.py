def substring(arr):
    max_length = 0
    start = 0
    hashmap = {}

    for i in range(len(arr)):
        if arr[i] in hashmap:
            start = max(start, hashmap[arr[i]] + 1)
        
        hashmap[arr[i]] = i
        max_length = max(max_length, i - start + 1)
    
    return max_length

str = "bacabcbb"
print(substring(str)) # output - 3