def solution(n):
    s = str(n)
    number_list = sorted(list(s), reverse=True)
    answer = int("".join(number_list))
    
    return answer