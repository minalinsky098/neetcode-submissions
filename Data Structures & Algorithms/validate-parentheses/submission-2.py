class Solution:
    def isValid(self, s: str) -> bool:
        valid_p = {')': '(', '}':'{', ']':'['}
        seen = []
        print(s)
        for i in s:
            if i in valid_p.values():
                seen.append(i)
            elif i in valid_p.keys():
                if not seen:
                    return False
                if valid_p[i] != seen[-1]:
                    return False
                seen.pop() 
        if not seen:
            return True
        return False
