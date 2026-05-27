class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            l,r = i+1 , len(nums)-1
            while l < r:

                if nums[l] + nums[r] + nums[i] == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1 
                    r -= 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        
        return [list(x) for x in res]                    