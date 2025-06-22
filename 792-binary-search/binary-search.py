class Solution(object):
    def search(self, nums, target):
        #Dom
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) -1

        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return nums.index(target)
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return -1

