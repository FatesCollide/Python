class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:      
        length = len(strs[0])
        for x in range(1, len(strs)):
            length = min(length, len(strs[x]))
            while length > 0 and strs[0][0:length] != strs[x][0:length]:
                length -= 1
            if length == 0:
                return ""
        return strs[0][0:length]
