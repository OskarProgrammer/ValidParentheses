class Solution:
    def isValid(self, s: str) -> bool:
        lista = []
        opening = ["(","[","{"]
        for x in s:
            if x in opening:
                lista.append(opening[opening.index(x)])
            else:
                if not lista:
                    return False
                if x == ')' and lista[-1] == '(':
                    lista.pop()
                elif x == '}' and lista[-1] == '{':
                    lista.pop()
                elif x == ']' and lista[-1] == '[':
                    lista.pop()
                else:
                    return False
        return not lista