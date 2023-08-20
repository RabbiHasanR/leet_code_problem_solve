class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_index = 0
        typed_index = 0
        last_char = None
        if len(typed) < len(name):
            return False

        while typed_index < len(typed):
            if name[name_index] == typed[typed_index]:
                last_char = name[name_index]
                if name_index < len(name) - 1:
                    name_index += 1
                typed_index += 1
                    
            elif last_char == typed[typed_index]:
                typed_index += 1
                
            else:
                return False
        return name_index + 1 == len(name) and name[-1] == typed[-1]