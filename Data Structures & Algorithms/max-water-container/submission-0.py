class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        maximum_area = 0

        while l < r:
            width = r - l #(r in larger index)
            height = min(heights[l], heights[r])
            current_area = width*height
            maximum_area = max(maximum_area, current_area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maximum_area





        