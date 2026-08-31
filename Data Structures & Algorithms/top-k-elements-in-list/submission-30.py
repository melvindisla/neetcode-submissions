class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1
        freq_map = {}
        # THIS IS KEY !!!!
        freq_list = [[] for i in range(len(nums) + 1)]
        #Step 2
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for element, frequency in freq_map.items():
            freq_list[frequency].append(element)
        # Step 3: create the empty are
        results = []
        
        # Step 4: loop through the indexes of the outer list in reversed
        for idx in range(len(freq_list) - 1, 0, -1):
            # loop through the list of elements at every index
            for element in freq_list[idx]:
                results.append(element)
                if len(results) == k:
                    return results
        
        return results        