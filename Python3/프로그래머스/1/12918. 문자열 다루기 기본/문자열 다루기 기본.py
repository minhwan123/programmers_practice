# 방법 1
def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False
    
# 방법 2
# def solution(s):
#     if len(s) != 4 and len(s) != 6:
#         return False

#     nums = "0123456789"
#     for char in s:
#         if char not in nums:
#             return False
            
#     return True