import math

def solution(a, b):
    
    gcd = math.gcd(a, b)
    lcm = math.lcm(a, b)
    
    answer = [gcd, lcm]
    
    return answer

