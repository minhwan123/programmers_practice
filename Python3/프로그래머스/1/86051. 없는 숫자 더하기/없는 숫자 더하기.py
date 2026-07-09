# 방법 1
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

# # 방법 2
# def solution(numbers):
#     return 45 - sum(numbers)