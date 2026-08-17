class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for each in nums:
            if each in a:
                return True
            else:
                a.add(each)
        return False