class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        l = 0
        for r in range(len(nums)):
            if nums[r] > 0:
                swap(l,r)
                l += 1


            

        