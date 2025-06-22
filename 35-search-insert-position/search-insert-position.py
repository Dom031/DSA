class Solution(object):
    def searchInsert(self, nums, target):
        #Dom Test
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        count = 0

        while start <= end:
            mid = (start + end) // 2
            count += 1
            if nums[mid] == target:
                return nums.index(target)
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid -1
        return start


