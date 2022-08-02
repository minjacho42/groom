from math import gcd
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def circle(target, start, d):
            temp = target[start]
            dest = start + d
            if dest >= len(nums):
                dest -= len(nums)
            while dest != start:
                nums[dest], temp = temp, nums[dest]
                dest += d
                if dest >= len(nums):
                    dest -= len(nums)
            else:
                nums[start] = temp

        dist = k % len(nums)
        if dist == 0:
            return
        i_gcd = gcd(len(nums),dist)
        if i_gcd != 1:
            for i in range(i_gcd):
                circle(nums, i, dist)
        else:
            circle(nums, 0, dist)