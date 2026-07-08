class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        reversed_text = cleaned[::-1]

        return cleaned == reversed_text