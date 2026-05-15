class Solution:

    sep = '#'

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            lenght = len(i)
            s+=f'{lenght}{self.sep}{i}'
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != self.sep:
                j+=1

            lenght = int(s[i:j])

            word = s[j+1:j+1+lenght]
            res.append(word)
            i = j+1+lenght
        return res

