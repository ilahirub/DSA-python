'''
QUESTION:-
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

APPROACH:-
-> Calculate the optimum sum i.e. sum when all elements were present
-> Calculate the actual array's sum
-> Return the optimum sum - actual sum

// TIME COMPLEXITY = O(N)
// SPACE COMPLEXITY = O(0) '''
#
# nums = [3,0,1]
# n=3
# expected_sum = n * (n + 1) // 2
# actual_sum = sum(nums)
# print(expected_sum)
# print(actual_sum)
# print(expected_sum - actual_sum)

nums = [3,0,1]
n = len(nums)

for i in range(0, n+1):
    if i not in nums:
        print(i)

