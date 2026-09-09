class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y = str(x)
            for i in range(0, len(y) // 2):
                if y[i] != y[-(i + 1)]:
                    return False
            return True