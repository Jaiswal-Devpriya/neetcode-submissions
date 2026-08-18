class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        if len(s) != len(t):
            return False
        freq={}
        freqt={}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for j in range(len(t)):
            freqt[t[j]]=freqt.get(t[j],0)+1
        if freq == freqt:
            return True
        return False

