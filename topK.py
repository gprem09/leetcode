from collections import Counter
import heapq

def mostFreq(nums, k):
    count = Counter(nums)

    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (-freq, num))

    top_k = []
    for _ in range(k):
        top_k.append(heapq.heappop(heap)[1])

    return top_k

nums = [1, 2, 2, 3, 3, 3]
print(mostFreq(nums, 2))