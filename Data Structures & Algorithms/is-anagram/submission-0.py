class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ord_s = sorted(s)
        ord_t = sorted(t)
        #for i , j in zip(ord_s,ord_t):
        if ord_s == ord_t:
            return True
        else:
            return False
        