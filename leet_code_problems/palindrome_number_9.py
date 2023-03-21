class Solution:
    def isPalindrome(self, x: int) -> bool:
        lol = str(x)
        for index in range(len(lol)):
            if lol[index] != lol[-index - 1]:
                return False
        return True




