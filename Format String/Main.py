#Format String

#contoh generic
#string
nama = "imron syabani"
format_str=f"hello {nama}"
print(format_str)

# boolean
bool = True
format_str=f"Ini Boolean {bool}"
print(format_str)

#angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# Bilangan Bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str=f"Rp.{angka:,}"
print(format_str)

# bilangan desimal
angka = 2000000.5
format_str=f"Desimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2000000.422323
format_str=f"desimal = {angka:019.3f}"
print(format_str)

# menampilkan tanda + atau -
minus = -10
plus = 10
format_minus=f"minus = {minus:+d}"
format_plus=f"plus = {plus:+d}"

print(format_minus)
print(format_plus)

# memformat % persen
persen=0.045
format_persen=f"persen = {persen:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga=10000
jumlah=5

format_str=f"Harga Total = Rp.{harga*jumlah:,}"
print(format_str)


