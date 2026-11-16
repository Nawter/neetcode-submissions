class Solution:

    def encode(self, strs: List[str]) -> str:
        # from list of strings to string
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)
            

    def decode(self, s: str) -> List[str]:
        # from string to list of strings
        i=0
        res = []

        while i < len(s):
            j = i 

            while s[j] != "#":
                j = j + 1
            
            length = int(s[i:j])
            i = j + 1
            j = length + i

            res.append(s[i:j])
            
            i = j
        
        return res

        


