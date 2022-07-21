class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = []
        length = 0
        for c in s:
            if c in string:
                if len(string) > length:
                    length = len(string)
                string = string[string.index(c)+1:]
                string.append(c)
            else:
                string.append(c)
        else:
            if len(string) > length:
                length = len(string)
        return length