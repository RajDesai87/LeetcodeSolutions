class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1,s2=[],[]
        for char in s:
            if s1:
                if char=='#':
                    s1.pop()
                else:
                    s1.append(char)
            else:
                if char!='#':
                    s1.append(char)
        for char in t:
            if s2:
                if char=='#':
                    s2.pop()
                else:
                    s2.append(char)
            else:
                if char!='#':
                    s2.append(char)
        return ''.join(s1)==''.join(s2)