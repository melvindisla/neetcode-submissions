class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        product = 1
        excluded_index = 0
        
        for i in range(len(nums)):
                
            for i in range(len(nums)):
                
                if i == excluded_index:
                    continue
                else:
                    product *= nums[i]

            output.append(product)
            product = 1
            excluded_index += 1
        return output
            
            

    
            