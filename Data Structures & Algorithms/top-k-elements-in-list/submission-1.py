class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        visited = dict()
        for each in nums:
            if each not in visited:
                visited[each] = 1
            else:
                visited[each] += 1
        
        sorted_tuples = sorted(visited.items(), 
        key=lambda item: item[1], reverse=True)
        a = [each[0] for each in sorted_tuples[:k] ]
        return a

