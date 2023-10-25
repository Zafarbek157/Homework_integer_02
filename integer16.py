# 3 xonali butun son berilgan. Berilgan birlik va o'nlik raqamlarini almashtirish orqaliolingan butun sonni chiqaring. 123-132 ga o'zgartiriladi
A=int(input("3 xonali sonni kiriting"))
Z=A//100 # 1-xona
S=(A//10)%10 # 2-xona
K=S%10 # 3-xona
M=K*100+Z*10+S
print(M)