class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            sorted_str = ''.join(sorted(i))
            if not res.get(sorted_str) is None:
                res[sorted_str].append(i)
            else:
                res[sorted_str] = [i]

        return list(res.values())