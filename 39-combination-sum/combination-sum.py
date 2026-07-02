class Solution:
    def __init__(self):
        self.answer = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking([], candidates, target, 0)
        return self.answer
    
    def backtracking(self, combination, candidates, target, order):
        if sum(combination) == target:
            self.answer.append(combination)
            return
        
        for idx, candidate in enumerate(candidates[order:]):
            if sum(combination) + candidate <= target:
                self.backtracking(combination + [candidate], candidates, target, order + idx)