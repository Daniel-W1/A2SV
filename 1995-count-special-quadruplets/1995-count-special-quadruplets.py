class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j + 1, len(nums)):
                    cur = nums[i] + nums[j] + nums[k]
                    for final in range(k +1, len(nums)):
                        if nums[final] == cur:
                            ans += 1
        
        return ans