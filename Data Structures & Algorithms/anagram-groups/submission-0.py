class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # original thought:
        # create dict, key -> str, value -> anagrams
        # for each str, create dict, key -> char, value -> count
        # if anagram, add to dict
        # at end, print only values from dict

        # actual O(m*n) solution

        # defaultdict assigns set value to keys that dont yet exist
        result = defaultdict(list) # key -> charCount list, value -> list of anagrams

        for str in strs:
            # create char array for each string
            count = [0] * 26 # list for a -z

            # frequency of each character in the string using ascii (ord)
            for char in str:
                count[ord(char) - ord("a")] += 1

            # add str to the value for the count array key
            result[tuple(count)].append(str)

        return list(result.values()  )      


