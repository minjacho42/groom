class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i_min = 0
        i_max = len(nums)-1
        i_half = int((i_min + i_max)/2)
        while i_min < i_max:
            if nums[i_half] == target:
                return i_half
            if nums[i_half] > target:
                i_max = i_half - 1
            else:
                i_min = i_half + 1
            i_half = int((i_min + i_max)/2)
        else:
            if i_min == i_max and nums[i_min] == target:
                return i_min
        return -1