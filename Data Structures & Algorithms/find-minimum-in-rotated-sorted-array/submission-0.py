class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimun = nums[0]
        for i in range(len(nums)):
            if nums[i] < minimun:
                minimun = nums[i]
        return minimun 
        