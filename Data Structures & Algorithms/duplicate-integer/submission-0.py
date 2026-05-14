class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set()

        for i in nums:
            if not i in n:
                n.add(i)
                continue
            return True
        return False
            