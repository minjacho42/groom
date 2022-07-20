class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        flag = False
        
        for i,c in enumerate(s2):
            if c in s1: