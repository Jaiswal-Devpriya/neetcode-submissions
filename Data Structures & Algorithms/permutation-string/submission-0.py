class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        freq={}
        window_freq_s2 = {}
        k = len(s1)

        for ch in s1:
            freq[ch] = freq.get(ch,0) + 1
        for right in range(len(s2)):
            window_freq_s2[s2[right]]= window_freq_s2.get(s2[right],0)+1
            if right-left+1 == k:
                if freq == window_freq_s2:
                    return True

                window_freq_s2[s2[left]] -= 1
                if window_freq_s2[s2[left]] == 0:
                    del window_freq_s2[s2[left]]
                left+=1
        return False

        


            

        