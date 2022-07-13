# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i_min = 1
        i_max = n
        i_mid = int((i_min+i_max)/2)
        while True:
            if isBadVersion(i_mid):
                i_max = i_mid
            else:
                i_min = i_mid+1
            i_mid = int((i_min+i_max)/2)
            if i_min==i_max:
                return i_min