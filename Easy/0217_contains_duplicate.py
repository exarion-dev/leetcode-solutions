# Problem Link: https://leetcode.com/problems/contains-duplicate
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
