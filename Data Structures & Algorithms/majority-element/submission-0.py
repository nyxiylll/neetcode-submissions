class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i,0) + 1
            if hash_map[i] >= len(nums) / 2:
                return i
        
        