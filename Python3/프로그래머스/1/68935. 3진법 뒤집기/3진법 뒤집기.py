def solution(n):

    three_n = ""
    while n > 0:
        n, remainder = divmod(n, 3)
        three_n += str(remainder)

    return int(three_n, 3)