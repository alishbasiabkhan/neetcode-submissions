class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0

        while left < right:
            # area = widht * height
            area = (right - left) * min(heights[right], heights[left])
            maxArea = max(area, maxArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea


        