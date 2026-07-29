class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            needed_num = target- num
            if needed_num in seen:
                return [seen[needed_num],i]

            else:
                seen[num]=i