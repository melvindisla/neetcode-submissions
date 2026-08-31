class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequencies = [[] for i in range(len(nums)+1)]
        results = []

        for element, freq in count.items():
            frequencies[freq].append(element)
        
        for idx in range(len(frequencies)-1, 0, -1):
            for val in frequencies[idx]:
                results.append(val)
                if len(results) == k:
                    return results