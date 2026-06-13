import string
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alphabet = list(string.ascii_lowercase)
        r_alphabet = alphabet.copy()
        r_alphabet.reverse()
        answer = ''
        for word in words:
            letter_number = 0
            for letter in word:
                letter_number += weights[alphabet.index(letter)]
            else:
                letter_number %= 26
                answer += r_alphabet[letter_number]

        
        return answer