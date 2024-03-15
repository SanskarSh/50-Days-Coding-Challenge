from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    result.append([i, j])
        return result

arr = [2, 7, 11, 15, 3, 6, 8, 9, 10, 12, 13, 14, 16]
target = 9
print(twoSum(None, arr, target))
