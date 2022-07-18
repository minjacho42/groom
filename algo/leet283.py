class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                n += 1
            else:
                nums.append(nums[i])
        del nums[:length]
        for i in range(n):
            nums.append(0)