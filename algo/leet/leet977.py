
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for num in sorted(nums, key=lambda x : x**2):
            result.append(num**2)
        return result