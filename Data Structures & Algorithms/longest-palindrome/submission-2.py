class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=0
        hasodd=False
        freq={}
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0)+1
        for value in freq.values():
            
            
            if ((value % 2) == 0):
                count+=value
            else:
                count +=(value-1)
                hasodd=True
        if hasodd == True:
            count += 1
        
        

        return count
