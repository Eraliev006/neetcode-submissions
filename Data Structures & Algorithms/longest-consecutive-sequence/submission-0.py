class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for i in nums_set:
            if i - 1 in nums_set:
                continue
            
            current_len = 1
            while i + current_len in nums_set:
                current_len += 1

            longest = max(current_len, longest)
        return longest