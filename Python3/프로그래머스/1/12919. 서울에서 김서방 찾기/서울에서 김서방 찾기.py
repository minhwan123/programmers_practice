# 방법 1
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 " + str(i) + "에 있다"

# 방법 2 
# def solution(seoul):
#     i = seoul.index("Kim")
#     return f"김서방은 {i}에 있다"
        