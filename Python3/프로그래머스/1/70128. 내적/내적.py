# 방법 1
def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j 
    return answer

# # 방법 2
# def solution(a, b):
#     answer = 0
#     for i in range(len(a)):
#         answer += a[i] * b[i]
#     return answer