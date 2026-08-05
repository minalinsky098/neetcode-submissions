class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        anagrams = []
        hashlist = []
        for i in strs:
            for j in i:
                if j not in hashmap:
                    hashmap[j] = 1
                else:
                    hashmap[j] += 1
            if hashmap in hashlist:
                anagrams[hashlist.index(hashmap)].append(i)
                hashmap = {}
                continue
            else:
                hashlist.append(hashmap)
            hashmap = {}
            anagrams.append([i])
        return anagrams