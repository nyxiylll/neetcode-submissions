class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        tot = []
        for i in range(len(nums)-k+1):
            window = nums[i : k + i]
            max_val = max(window)
            tot.append(max_val)
        return tot

            




        