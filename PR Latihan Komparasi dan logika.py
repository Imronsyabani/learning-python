#Tugas 1
#-------0+++++++5------8++++++11------
print(5*'=','Tugas 1')
angka = float(input('Masukkan Angka: '))

kecilDari0 = angka < 0
print('Kurang Dari 0:',kecilDari0)
besarDari0 = angka > 0
print('Besar Dari 0:',besarDari0)
besarDari5 = angka > 5
print('Besar Dari 5:',besarDari5)
kecilDari5 = angka < 5
print('Kurang Dari 5:',kecilDari5)
besarDari8 = angka > 8
print('Besar Dari 8:',besarDari8)
kecilDari8 = angka < 8
print('Kurang Dari 8:',kecilDari8)
besarDari11 = angka > 11
print('Besar Dari 11:',besarDari11)
kecilDari11 = angka < 11
print('Kurang Dari 11:',kecilDari11)

isCorrect = besarDari0 and kecilDari5 or besarDari8 and kecilDari11
print('Memasukan angka:',isCorrect)
#Tugas 2
#++++++0--------5++++++8-------11++++++
print('\n',5*'=','Tugas 2')
angka = float(input('Masukkan Angka: '))

kecilDari0 = angka > 0
print('Kurang Dari 0:',kecilDari0)
besarDari0 = angka < 0
print('Besar Dari 0:',besarDari0)
besarDari5 = angka > 5
print('Besar Dari 5:',besarDari5)
kecilDari5 = angka < 5
print('Kurang Dari 5:',kecilDari5)
besarDari8 = angka > 8
print('Besar Dari 8:',besarDari8)
kecilDari8 = angka < 8
print('Kurang Dari 8:',kecilDari8)
besarDari11 = angka < 11
print('Besar Dari 11:',besarDari11)
kecilDari11 = angka > 11
print('Kurang Dari 11:',kecilDari11)

isCorrect = besarDari0 and kecilDari5 or besarDari8 and kecilDari11
print('Memasukan angka:',isCorrect)