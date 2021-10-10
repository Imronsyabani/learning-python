# date and time (latihan)

import datetime as dt

# today = dt.date.today()
# print(today)

# tanggal = dt.date(2002,10,5)
# print(tanggal)
# print(f"Tanggal 05 di tahun 2002 adalah hari = {tanggal:%A}")

print("Silahkan masukkan tanggal bulan dan tahun lahir anda")
tanggal = int(input("Masukkan tanggal lahir:"))
bulan = int(input("Masukkan bulan: "))
tahun = int(input("Masukkan tahun "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal Lahir Anda = {tanggal_lahir}")
print(f"Hari Nya Adalah = {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal:{hari_ini}")
umur = hari_ini - tanggal_lahir
umur_tahun = umur.days // 365
print(f"Umur Anda:{umur_tahun:} Tahun")