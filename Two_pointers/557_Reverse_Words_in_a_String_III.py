class Solution:
    def reverseWords(self, s: str) -> str:
        #first solution with one pointer
        # word_list = s.split()
        # last_index = len(word_list) - 1
        # word = ''

        # index = len(s) - 1

        # while index >= 0:
        #     if s[index].isspace():
        #         word_list[last_index] = word
        #         last_index -= 1
        #         word = ''
        #         index -= 1
        #     else:
        #         word += s[index]
        #         index -= 1
        # if index == -1:
        #     word_list[last_index] = word
        # return ' '.join(word_list)
        #secon solution with two pointers
        reverse_string = ''
        left = right = 0

        while right < len(s):
            if s[right] != ' ':
                right += 1
            else:
                reverse_string += s[left:right+1][::-1]
                right += 1
                left = right
        reverse_string += ' '
        reverse_string += s[left:right+1][::-1]
        return reverse_string[1:]
    

class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_string = ''
        left = right = 0
        while right < len(s):
            if s[right] != ' ':
                right += 1
            else:
                reverse_string += s[left:right+1][::-1]
                right += 1
                left = right
        reverse_string += ' '
        reverse_string += s[left:right+1][::-1]
        return reverse_string[1:]