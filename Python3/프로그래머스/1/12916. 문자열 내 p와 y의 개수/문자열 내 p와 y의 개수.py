#방법 1
import re
def solution(s):
    p_count = len(re.findall(r'p', s, re.IGNORECASE))
    y_count = len(re.findall(r'y', s, re.IGNORECASE))
    
    answer = (p_count == y_count)
    
    return answer


# 방법 2
# def solution(s):
#     s = s.lower()
#     return s.count('p') == s.count('y')
