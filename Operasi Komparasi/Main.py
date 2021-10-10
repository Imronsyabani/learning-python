# Operasi Komparasi
# Setiap hasil dari komparasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print("====== Lebih Besar Dari (>)")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# Kurang dari <
print("====== Kecil Dari (<)")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih dari sama dengan >=
print("====== Kecil Dari Sama Dengan (>=)")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# Kurang dari sama dengan >=
print("====== Kecil Dari Sama Dengan (<=)")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# Sama dengan ==
print("====== Sama Dengan (==)")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)

# Tidak Sama dengan !=
print("====== Tidak Sama Dengan (!=)")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)

# 'is' sebagai komaprasi object identity
print("====== Object Identity (is)")
x = 5 # ini nilai assigment membuat objek
y = 5
print("nilai x =",x,'id = ',hex(id(x)))
print("nilai y =",y,'id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
print("====== Object Identity (is not)")
x = 5 # ini nilai assigment membuat objek
y = 6
print("nilai x =",x,'id = ',hex(id(x)))
print("nilai y =",y,'id = ',hex(id(y)))
hasil = x is not 6
print('x is y =',hasil)