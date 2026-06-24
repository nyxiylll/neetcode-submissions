class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set = set()
        for i in nums:
            if i not in hash_set:
                hash_set.add(i)
            else:
                hash_set.remove(i)
        return hash_set.pop()
        