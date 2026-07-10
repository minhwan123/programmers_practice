def solution(phone_number):
    change = phone_number[:-4]
    change_len = len(phone_number) - 4
    phone_number = phone_number.replace(change, "*" * change_len)
    return phone_number