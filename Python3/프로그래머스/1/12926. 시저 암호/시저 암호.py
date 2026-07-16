def solution(s, n):
    answer = ''
    
    for char in s:
        if char == ' ':
            answer += ' '

        elif char.islower():
            shifted = (ord(char) - ord('a') + n) % 26
            answer += chr(shifted + ord('a'))
            
        elif char.isupper():
            shifted = (ord(char) - ord('A') + n) % 26
            answer += chr(shifted + ord('A'))
            
    return answer