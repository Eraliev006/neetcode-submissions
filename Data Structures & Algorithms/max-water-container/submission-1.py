class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1

        max_amount = 0

        while l < r:
            amount = (r - l) * min(heights[r], heights[l])

            if heights[r] > heights[l]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            else:
                l+=1
                r-=1

            max_amount = max(max_amount, amount)

        return max_amount
