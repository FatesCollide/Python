class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        cnt = {}

        for ch in ransomNote:
            cnt[ch] = cnt.get(ch, 0) - 1

        for ch in magazine:
            cnt[ch] = cnt.get(ch, 0) + 1

        
        for num in cnt.values():
            if num < 0:
                return False
            
        return True
           
        

        


