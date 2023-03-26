class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        split_list = s.split()

        return len(split_list[-1])
