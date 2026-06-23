class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        left = 0
        count = float('inf')

        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum >= target:
                count = min(count, right - left + 1)
                # print('currentSum:', currentSum, 'count:', count, 'left:', left, 'right:', right)
                currentSum -= nums[left]
                left += 1
        return count if count != float('inf') else 0

        