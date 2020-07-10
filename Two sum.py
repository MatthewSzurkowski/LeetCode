#Two Sum


##Given an array of integers, return indices of
##the two numbers such that they add up to a specific target.
##You may assume that each input would have exactly
##one solution, and you may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            n = i + 1
            if (i+1 > len(nums)):
                n = 0
            for j in range(n, len(nums)):
                if (nums[j] + nums[i] == target):
                    return [j, i]
