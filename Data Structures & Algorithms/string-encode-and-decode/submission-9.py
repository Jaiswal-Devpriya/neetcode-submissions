class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the '#'
            while s[j] != "#":
                j += 1

            # Length of the next string
            length = int(s[i:j])

            # Extract the string
            res.append(s[j + 1 : j + 1 + length])

            # Move to the next encoded string
            i = j + 1 + length

        return res