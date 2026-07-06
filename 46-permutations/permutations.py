class Solution:
    def __init__(self):
        self.answer = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, [])
        return self.answer
    
    def backtracking(self, nums, permutation):
        if len(permutation) is len(nums):
            self.answer.append(permutation)
            return
        
        for num in nums:
            if num not in permutation:
                self.backtracking(nums, permutation + [num])