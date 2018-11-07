def checkio(get_code):
    print("请输入您的密码：")
    get_code = input()
    n = len(get_code)
    c_num = 0
    c_a = 0
    c_A = 0
    if n < 10:
        return False
    for i in range(0,n):
        if ord(get_code[i]) >= ord('A') and ord(get_code[i]) <= ord('Z'):
            c_A += 1
        elif ord(get_code[i]) >= ord('a') and ord(get_code[i]) <= ord('z'):
            c_a += 1
        else:
            c_num += 1
        if c_num != 0 and c_a != 0 and c_A != 0:
            return True
    return False   

if __name__ == "__main__":
    get_code = list(range(50))
    print(checkio(get_code))
    
