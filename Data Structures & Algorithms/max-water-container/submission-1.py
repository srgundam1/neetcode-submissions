class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE
        # area = 0

        # for l in range(len(heights)):
        #     for r in range(l+1, len(heights)):
        #         currArea = (r-l) * min(heights[l], heights[r])
        #         area = max(area, currArea)
        # return area

        # optimal
        res =0 # max area
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            res = max(res, area)
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        return res