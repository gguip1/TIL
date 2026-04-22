class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = ''.join(reversed(x))

        if x == y:
            return True
        
        return False