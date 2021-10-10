# Program Konversi celcius ke satuan lain

print("### PROGRAM KONVERSI TEMPERATUR ###")
# celcius = float(input("Masukan Nilai Celcius:"))
# print("suhu adalah",celcius,"Celcius")

# #Reamur
# reamur = (4/5) * celcius
# print("suhu celcius dalam reamur adalah:",reamur,"reamur")

# #Fahrenheit
# fahrenheit = ((9/5) * celcius) + 32
# print("suhu celcius dalam fahrenheit adalah:",fahrenheit,"fahrenheit")

# #Kelvin
# kelvin = celcius + 273
# print("suhu celcius dalam kelvin adalah:",kelvin,"kelvin")

suhu = float(input("Masukan Nilai Suhu:"))
kelvin = suhu + 273
print("Suhu fahrenheit ke kelvin adalah",kelvin,"kelvin")
fahrenheit = ((5/9) * suhu) + 32
print("Suhu fahrenheit ke kelvin adalah",fahrenheit,"kelvin")