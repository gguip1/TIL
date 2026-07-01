class Solution:
    def __init__(self):
        self.answer = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtracking('', 0, 0, n)
        return self.answer

    def backtracking(self, parentheses, check1, check2, n):
        if check1 == n and check2 == n:
            self.answer.append(parentheses)
            return
        
        if check1 < n:
            self.backtracking(parentheses + '(', check1 + 1, check2, n)

        if check2 < check1:
            self.backtracking(parentheses + ')', check1, check2 + 1, n)
            