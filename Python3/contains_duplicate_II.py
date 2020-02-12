class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1: return False
        
        hashmap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashmap and abs(i-hashmap[nums[i]]) <= k: 
                return True
            hashmap[nums[i]] = i
            
        return False
