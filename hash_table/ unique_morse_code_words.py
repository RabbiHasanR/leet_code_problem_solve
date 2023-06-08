from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet_dict = {}
        morse = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        count = 0
        result = set()
        for i in range(ord('a'), ord('z') + 1):
            alphabet_dict[chr(i)] = morse[count]
            count += 1
        for word in words:
            code = ''
            for c in word:
                code += alphabet_dict[c]
            result.add(code)
        return len(result)