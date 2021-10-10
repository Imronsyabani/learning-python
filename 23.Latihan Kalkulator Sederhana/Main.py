# Kalkulator Sederhana Menggunakan If Elif Dan Else

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukkan Angka: "))
operator = input("Operator(+,-,*,/) : ")
angka_2 = float(input("Masukan Angka: "))

# Percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya Adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya Adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya Adalah {hasil}")
else:
    print("Salah Masukan Angka")
print("---Selamat Menikmati---")