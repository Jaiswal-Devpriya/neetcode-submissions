class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        # Visit every word one by one.
        for word in strs:

            # Store:
            # length of word + '#' + actual word.
            # Example:
            # "Hello" -> "5#Hello"
            encoded += str(len(word)) + "#" + word

        # Return the complete encoded string.
        return encoded

    def decode(self, s: str) -> List[str]:
        # This will store the decoded strings.
        result = []

        # Pointer that walks through the encoded string.
        i = 0

        # Continue until we've processed the whole string.
        while i < len(s):

            # j is used to locate the '#' separator.
            j = i

            # Move j until we find '#'.
            while s[j] != "#":
                j += 1

            # Characters from i to j represent the length.
            length = int(s[i:j])

            # The actual word starts immediately after '#'.
            start = j + 1

            # The word ends after 'length' characters.
            end = start + length

            # Extract the word and add it to the answer.
            result.append(s[start:end])

            # Move i to the beginning of the next encoded word.
            i = end

        # Return the reconstructed list.
        return result
