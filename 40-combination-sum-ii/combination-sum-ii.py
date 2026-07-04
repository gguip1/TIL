class Solution:
    def __init__(self):
        self.answer = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(sorted(candidates), target, [], 0)
        return self.answer

    def backtracking(self, candidates, target, candidate, order):
        if target == 0:
            self.answer.append(candidate)
            return

        for idx in range(order, len(candidates)):
            if candidates[idx] > target:
                break
            
            if idx > order and candidates[idx] == candidates[idx - 1]:
                continue

            self.backtracking(candidates, target - candidates[idx], candidate + [candidates[idx]], idx + 1)


