class Solution:
    def countCompleteSubarrays(self, nums):
        
        # Find total number of distinct elements
        total_distinct = len(set(nums))
        
        # Exactly K distinct = atMost(K) - atMost(K-1)
        return self.atMost(nums, total_distinct) - self.atMost(nums, total_distinct - 1)

    
    def atMost(self, nums, k):
        if k == 0:
            return 0
        
        freq = {}
        left = 0
        count = 0
        
        for right in range(len(nums)):
            
            # Add current element
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # Shrink window if distinct elements > k
            while len(freq) > k:
                
                freq[nums[left]] -= 1
                
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                
                left += 1
            
            # Number of valid subarrays ending at right
            count += right - left + 1
        
        return count