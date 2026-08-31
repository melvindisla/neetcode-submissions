class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: need a count map: used to keep track of the frequency of each element
        # step 2: we need a nested lists, where the outer tracks the frequency and the inner is a list of elemnents
        # with that frequency
        # step 3: create a results array

        # step 4: populate the map, and populate the nested list from the map

        # step 5: iterate in reverse through the nested list, by index, then iterate through the list of that index
        # step 6: append the num to the results array and then check if the length of the results 

        count = {}
        frequencies = [[] for i in range(len(nums)+1)]
        results = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for element, freq in count.items():
            frequencies[freq].append(element)
        
        for idx in range(len(frequencies)-1, 0, -1):
            for val in frequencies[idx]:
                results.append(val)
                if len(results) == k:
                    return results