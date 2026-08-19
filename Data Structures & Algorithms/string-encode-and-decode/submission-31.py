class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += f"{len(i)}#{i}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        count = 0
        last_read = 0
        i = 0
        while i < (len(s)):
            if s[i] == "#":
                count = int(s[last_read:i])
                decoded.append(s[i+1:i+1+count])
                last_read = i+1+count
                i += count+1
            else:
                i += 1
        return decoded
    