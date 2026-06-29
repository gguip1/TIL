class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        answer = 0
        for pattern in patterns:
            if self.solve(pattern, word):
                answer += 1
        return answer
    
    def solve(self, pattern: str, word: str) -> boolean:
        for i in range(len(word) - len(pattern) + 1):
            if word[i:len(pattern) + i] == pattern:
                return True
        return False
