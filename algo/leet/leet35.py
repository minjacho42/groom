class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i_max = len(nums) - 1
        i_min = 0
        index = int((i_max+i_min)/2)
        while i_min < i_max:
            if nums[index] == target:
                return index
            if nums[index] > target:
                i_max = index
            else:
                i_min = index + 1
            index = int((i_max+i_min)/2)
        else:
            if nums[index] == target:
                return index
            if nums[index] > target:
                return index
            else:
                return index + 1