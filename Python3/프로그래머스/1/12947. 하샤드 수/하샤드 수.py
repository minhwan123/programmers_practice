def solution(x):
    digits = [int(i) for i in str(x)]
    if x % sum(digits) == 0:
        return True
    else:
        return False