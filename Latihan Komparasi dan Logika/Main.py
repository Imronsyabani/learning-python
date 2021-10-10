# Latihan Logika dan Komparasi

#++++++++3=========10++++++++

inputUser = float(input("masukan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10 \n:"))

# +++++++++3============
#Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('Kurang dari 3 = ',isKurangDari)

isLebihDari = (inputUser > 10)
print('Lebih dari dari 10 = ',isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukan:',isCorrect)

#======3+++++++10======
#kasus irisan
print('\n',10*'=','\n')
inputUser = float(input("masukan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10 \n:"))

#====3++++++++
#lebih dari 3
isLebihDari = inputUser > 3
print('lebih dari 3: ',isLebihDari)
#++++++++10=======
isKurangDari = inputUser < 10
print('lebih dari 10: ',isKurangDari)

isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukkan: ',isCorrect)