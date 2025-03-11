class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = set()

        for item in nums:
            if item in hash_table:
                return True
            else:
                hash_table.add(item)
            
        return False