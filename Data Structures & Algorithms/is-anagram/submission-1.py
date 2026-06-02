class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ord_s = sorted(s)
        ord_t = sorted(t)
        if ord_s != ord_t:
            return False
        else:
            return True
        