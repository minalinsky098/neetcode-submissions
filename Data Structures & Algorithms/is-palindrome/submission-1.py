class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.upper()
        for i in range(len(s)):
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            print(s[left], s[right])
            if s[left] != s[right]:
                return False
            elif left == right:
                return True
            left += 1
            right -= 1
        return True