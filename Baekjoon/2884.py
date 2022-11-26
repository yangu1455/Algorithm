# 2884번 알람 시계

H, M= map(int, input().split())
if H == 0:
    if M >= 45:
        M= M-45
        print(H, M)
    else:
        H= 23
        M= 60+M-45
        print(H, M)
            
elif H != 0:
    if M >= 45:
        M= M-45
        print(H, M)
    else:
        H= H-1
        M= 60+M-45
        print(H, M)