class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = sorted(nums1 + nums2)
        n = len(new_list)
        
        if n % 2 == 0:
            middle1 = (n // 2) - 1
            middle2 = n // 2
            return (new_list[middle1] + new_list[middle2]) / 2
            
        else:
            middle = n // 2
            return new_list[middle]