class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        area = 0

        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                currArea = (r-l) * min(heights[l], heights[r])
                area = max(area, currArea)
        return area