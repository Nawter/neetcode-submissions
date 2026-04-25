class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        nums.sort()
        
        for elem in nums:
            map[elem] = 1 + map.get(elem, 0)

        arry = []
        for elem, count in map.items():
            arry.append([count, elem])
        arry.sort()
        
        result = []
        while len(result) < k:
            result.append(arry.pop()[1])

        return result
