class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        start = 0
        started = False
        sample = list(s1)
        while i < len(s2):
            c = s2[i]
            if c in sample:
                if not started:
                    started = True
                    start = i
                sample.remove(c)
                if len(sample) == 0:
                    return True
            elif started:
                if c in s1:
                    sample.append(s2[start])
                    if len(sample) == len(s1):
                        started = False
                    else:
                        start += 1
                    i -= 1
                else:
                    started = False
                    sample = list(s1)
            i += 1
        return False