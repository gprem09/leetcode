from collections import defaultdict

def groupAnagram(str):
    result = defaultdict(list)
    for s in str:
        count = [0] * 26
        for c in s:
            count[ord(c)-ord('a')] += 1
        result[tuple(count)].append(s)
    return result.values()

def groupAnagram_2(strs):
    grouped = {}
    for s in strs:
        sorted_word = "".join(sorted(s))
        if sorted_word in grouped:
            grouped[sorted_word].append(s)
        else:
            grouped[sorted_word] = [s]
    return list(grouped.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagram(strs))

