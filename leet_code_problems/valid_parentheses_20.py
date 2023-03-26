class Solution:
    def isValid(self, s: str) -> bool:

    	length = len(s)
    	x = 0
    	while x != length:
    		x = length
    		s = s.replace('()', '').replace('[]', '').replace('{}', '')    		    		
    		length = len(s)

    	return length == 0
        

