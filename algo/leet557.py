class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseString(word):
            string = list(word)
            end = len(string) - 1
            start = 0
            while start < end:
                string[start], string[end] = string[end], string[start]
                start += 1
                end -= 1
            return string
        texts = s.split()
        texts = list(map(reverseString,texts))
        text = ""
        for t in texts:
            text += ''.join(t) + ' '
        text = text.strip()
        return text