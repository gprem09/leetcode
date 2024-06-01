def isAnagram(a, b):
    # both should have the same characters - returns True
    # if not same character then returns False
    if len(a) != len(b):
        return False

    map_1 = {
        # a : 2
        # b : 2
    }
    map_2 = {
        # b : 3
        # a : 1
    }

    for i in range(len(a)):
        map_1[a[i]] = 1 + map_1.get(a[i], 0)

    for i in range(len(b)):
        map_2[b[i]] = 1 + map_2.get(b[i], 0)

    return map_1 == map_2
 

s = "abba"
t = "bbab"

x = "racecar"
y = "carrace"

print(isAnagram(s, t))
print(isAnagram(x, y))