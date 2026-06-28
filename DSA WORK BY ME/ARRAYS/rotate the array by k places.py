# nums = [1,2,3,4,5,6,7]
# k=int(input('enter k value: '))
#
# left=nums[:-k]
# right=nums[-k:]
#
# print(left)
# print(right)
# print(right+left)

''' Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]  '''

class solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        left=nums[:-k]
        right=nums[-k:]

        nums[:] = right+left