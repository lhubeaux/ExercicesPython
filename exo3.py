A = 13
B = 5
C = True
D = not(C)

result1 = (A > 10) and (B < 20)
print(result1)

result2 = (C != 40) or (D >= 100)
print(result2)

result3 = (A == 2) and (not (B > 15))
print(result3)

result4 = (C > 50) or (not(D < 200))
print(result4)

result5 = ((A < B) and (C > 30)) or (D == 270)
print(result5)

result6 = not ((A*B)>100)
print(result6)

result7 = ((B == 15) or ((C > 60) and (A < 5)))
print(result7)

result8 = (((B == 15) or ((C> 60) and (A < 2))) and (A < B)) or (not(B == 9))
print(result8)