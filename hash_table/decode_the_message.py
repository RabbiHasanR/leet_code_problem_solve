class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode_key = key.replace(" ", "")
        key_value = {}
        uni_code = ord('a')
        for i in range(len(decode_key)):
            if decode_key[i] not in key_value:
                key_value[decode_key[i]] = chr(uni_code)
                uni_code += 1
            
        
        mess = ''
        for c in message:
            if c.isspace():
                mess += ' '
            else:
                mess += key_value[c]
        return mess