# A,B,C 3 ta musbat sonlar berilgan. A B o'lchamdagi to'rtbrchakda yon uzunligi C bo'lgan kvadratlarning mumkin bo'lgan eng katta miqdori mavjud
# (bir-birini ustiga chiqmagan holda) To'rtburchakda joylashgan kvadratlar miqdorini va to'rtburchakning foydalanilmagan qismining maydonini top.
A=int(input(" musbat sonni kiriting "))
B=int(input(" musbat sonni kiriting "))
C=int(input(" musbat sonni kiriting "))
M=A*B # to'g'ri to'rtburchak yuzi
N=C*C # ichidagi kvadrat yuzi
S=M-N
print(S)