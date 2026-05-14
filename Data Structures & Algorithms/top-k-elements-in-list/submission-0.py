class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        bucket = Counter(nums)
        res = [[] for _ in range(len(nums) + 1)]

        for num, count in bucket.items():
            res[count].append(num)
        result = []
        
        for i in range(len(res) - 1, 0, -1):
            result.extend(res[i])
            if len(result) >= k:
                return result[:k]