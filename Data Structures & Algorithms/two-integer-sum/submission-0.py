class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevarray={}
        for i,num in enumerate(nums):
            thirdnumber=target-num
            if thirdnumber in prevarray:
                return[prevarray[thirdnumber],i]
            prevarray[num]=i