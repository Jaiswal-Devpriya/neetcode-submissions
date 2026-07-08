import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        S=s.lower()
        S = re.sub(r"[^a-zA-Z0-9]", "", S)
        reversed_text = S[::-1]
        if S == reversed_text:
            return True
        else:
            return False