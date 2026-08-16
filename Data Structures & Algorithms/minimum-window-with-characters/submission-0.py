class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        if not s or not t:
            return ""
        need = {}
        window = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:
                current_len = right - left + 1

                if current_len < min_len:
                    min_len = current_len
                    min_start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""
        return s[min_start:min_start + min_len]