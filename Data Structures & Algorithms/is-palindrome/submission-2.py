import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned_text = "".join(filter(str.isalnum, s))
        reversed_text = "".join(reversed(cleaned_text))
        
        return True if cleaned_text == reversed_text else False
