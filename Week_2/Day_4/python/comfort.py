class Solution:
    def isValid(self, s: str) -> bool:
        _stack = []        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                _stack.append(char)
            elif (char == ")" or char =="}" or char == "]") and len(_stack) != 0:
                if (_stack[-1] == "(" and char == ")") or (_stack[-1] == "{" and char == "}") or (_stack[-1] == "[" and char == "]") :

                    _stack.pop(-1)
                else: return False
            else:
                return False

        return len(_stack) == 0
    
        







        