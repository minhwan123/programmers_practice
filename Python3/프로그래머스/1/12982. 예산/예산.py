# 방법 1
def solution(d, budget):
    d.sort()
    count = 0
    
    for amount in d:
        if budget >= amount:
            budget -= amount
            count += 1
        else:
            break
            
    return count


# 방법 2
# def solution(d, budget):
#     d.sort()
#     count = 0
#     i = 0

#     while i < len(d) and budget >= d[i]:
#         budget -= d[i]
#         count += 1
#         i += 1
            
#     return count