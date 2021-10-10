# operasi dan manipulasi string

# 1.menyambung string (concate)
nama_depan = "imron"
nama_belakang = "syabani"

nama_lengkap = nama_depan +" "+ nama_belakang
print(nama_lengkap)

# 2. menghitung panjang string
panjang = print(len(nama_lengkap))

# 3. operator untuk string 

# mengecek apakah ada komponenen char atau di string 
d = "i"
status = d in nama_lengkap
print("apakah ada huruf",d,"di nama lengkap",status)

d = "I"
status = d in nama_lengkap
print("apakah ada huruf",d,"di nama lengkap",status)

d = "i"
status = d not in nama_lengkap
print("apakah tidak ada huruf",d,"di nama lengkap",status)

# mengulang string
print("wk"*10)
print(12*"wk")

# indexing
print("index ke-0 :"+nama_lengkap[0])
print("index ke-9 :"+nama_lengkap[9])
print("index ke-[-2] :"+nama_lengkap[-2]) #  mengambil data string dari belakang
print("index ke-[-6] :"+nama_lengkap[-6])
print("index ke-[0:5] :"+nama_lengkap[0:5]) # mengambil data dari range string
print("index ke-[0,2,4,6,8,10] :"+nama_lengkap[0:10:2]) # 

# item paling kecil
print("Paling kecil :" + min(nama_lengkap))
# item paling besar
print("Paling besar :" + max(nama_lengkap))

ascii_code = ord(" ")
print(" ASCII code untuk spasi adalah :" + str(ascii_code))
data = 177
print('char untuk 177 adalah ' + chr(data))

# 4. operator dalam bentuk method
data = "marcob mari kita coba"
jumlah = data.count("a")
print("jumlah a pada "+ data +" = " + str(jumlah))