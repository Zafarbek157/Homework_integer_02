# hafta kunlari quyidagicha raqamlangan : 0-yakshanba 1-dushanba 2-seshanba 3-chorshanba 4-payshanba 5-juma 6-shanba 
# 1 dan 365 gacha bo'lgan oraliqda butun son K berilgan. yilning K kuni uchun haftaning butun sonini toping. 
# agar bu yil 1-yanvar payshanba bo'lsa yilning K kumi uchun haftaning sonini toping
A=int(input(" K sonni kiriting 1<K<365 "))
Z=(A+4)%7
print(Z)