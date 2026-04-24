class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = {}

        for idx, num in enumerate(nums):
            if num not in groups:
                groups[num] = []
            groups[num].append(idx)

        print(groups)

        arr = [0] * len(nums)
        
        for indexes in groups.values():
            total = sum(indexes)
            prefix = 0
            count = len(indexes)
            for idx, index in enumerate(indexes):
                left = idx * index - prefix
                right = (total - prefix - index) - index * (count - idx - 1)

                arr[index] = left + right
                prefix += index
        
        return arr