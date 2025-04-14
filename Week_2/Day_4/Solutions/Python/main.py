class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bracketsMap = {")":"(", "}":"{" , "]": "["}
        stack = []

        for char in s:
            if char in bracketsMap.values():
                stack.append(char)
            elif char in bracketsMap.keys():
                if not stack or bracketsMap[char] != stack.pop():
                    return False
        return not stack

        