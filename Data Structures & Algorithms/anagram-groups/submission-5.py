class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        converted_strs = []
        for i in strs:
            sorted_str = "".join(sorted(list(i)))
            if anagrams:
                for j in anagrams:
                    sorted_j = "".join(sorted(list(j[0])))
                    if sorted_str == sorted_j:
                        j.append(i) 
                        break
                else:
                    anagrams.append([i])  
            else:
                anagrams.append([i])
        return anagrams