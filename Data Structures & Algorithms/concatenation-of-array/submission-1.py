class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = self._get_concatenation1(nums)
        # ans = self._get_concatenation2(nums, 2)
        # ans = self._get_concatenation3(nums, 2)

        ans = self._get_concatenation4(nums)

        return ans


    def _get_concatenation1(self, nums: List[int]) -> List[int]:
        return nums + nums


    def _get_concatenation2(self, nums: List[int], times: int) -> List[int]:
        return nums * times

    
    def _get_concatenation3(self, nums: List[int], times: int) -> List[int]:
        answ = []

        for i in range(times):
            for num in nums:
                answ.append(num)
        
        return answ



    

    def _get_concatenation4(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        answ = 2 * nlen * [0]

        for i in range(nlen):
            answ[i] = answ[i + nlen] = nums[i]
        
        return answ








    

        