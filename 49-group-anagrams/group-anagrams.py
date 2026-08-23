class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_dict = {}

        for word in strs:
                count = [0] * 26
                for char in word:
                    count[ord(char) - ord('a')] += 1
                key = tuple(count)
                if key in main_dict:
                    main_dict[key].append(word)
                else:
                    main_dict[key] = [word]

        return list(main_dict.values())