class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        aux = {}
        for num in nums:
            aux[num] = aux.get(num, 0) + 1
        
        arr = []
        for num, cnt in aux.items():
            arr.append([cnt, num])
        
        arr.sort()

        res = []

        for i in range(len(arr)):
            if i < k:
                res.append(arr.pop()[1])
        
        return res
        