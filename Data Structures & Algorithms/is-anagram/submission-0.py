class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1 = {i: s.count(i) for i in s}
        t1 = {i: t.count(i) for i in t}

        return s1 == t1