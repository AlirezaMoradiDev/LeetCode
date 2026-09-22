class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst_words = sentence.split(' ')
        size = len(searchWord)

        for word in lst_words:
            if searchWord in word[:size]:
                return lst_words.index(word) + 1
        
        else:
            return -1