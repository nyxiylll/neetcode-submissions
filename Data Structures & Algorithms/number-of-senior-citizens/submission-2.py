class Solution:
    def countSeniors(self, details: List[str]) -> int:
        total = 0
        for detail in details:
            window = detail[11:13]
            if int(window) > 60:
                total += 1
        return total
        