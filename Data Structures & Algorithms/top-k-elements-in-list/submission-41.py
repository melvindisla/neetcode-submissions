class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencies = [[] for i in range(len(nums)+1)]
        results = []

        count = Counter(nums)

        for element, freq in count.items():
            frequencies[freq].append(element)
        
        for idx in range(len(frequencies)-1, 0, -1):
            for val in frequencies[idx]:
                results.append(val)
                if len(results) == k:
                    return results