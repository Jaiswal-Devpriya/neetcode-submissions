class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # O(1) lookups instead of scanning the list
        if len(num_set) == 0:
            return 0
        
        longest = 0
        
        for num in num_set:
            current_num = num
            current_length = 1
            
            # try to extend the chain forward from THIS number
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            longest = max(longest, current_length)
        
        return longest