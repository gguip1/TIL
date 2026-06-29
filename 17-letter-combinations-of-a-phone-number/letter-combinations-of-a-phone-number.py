class Solution:
    def __init__(self):
        self.answer = []
        self.phone = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

    def letterCombinations(self, digits: str) -> List[str]:
        self.backtracking(digits, '', 0)
        return self.answer
    
    def backtracking(self, digits: str, letter: str, order: int):
        if order == len(digits):
            self.answer.append(letter)
            return
        
        for c in self.phone[digits[order]]:
            self.backtracking(digits, letter + c, order + 1)
