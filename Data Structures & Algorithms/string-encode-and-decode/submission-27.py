class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_arr = []
        for w in strs:
            encoded_w = f"{str(len(w))}@{w}"
            encoded_arr.append(encoded_w)

        return "".join(encoded_arr)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
        

