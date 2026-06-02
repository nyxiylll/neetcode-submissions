class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = []
        for i in range(len(nums)):
            if nums[i] in array:
                return True
            else:
                array.append(nums[i])
        return False
        