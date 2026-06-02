class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_char = [char.lower() for char in s if char.isalnum()]
        return cleaned_char == cleaned_char[::-1]
        