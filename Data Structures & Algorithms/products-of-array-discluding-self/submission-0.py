class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nl=[]
        
        for i in range(len(nums)):
            product =1
            for j in range(len(nums)):
                if i != j:
                    
                    product= product * nums[j]
            nl.append(product)
        return nl