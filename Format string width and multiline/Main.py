nama="Imron Syabani"
umur="19"
tinggi="169"
no_sepatu=44

#string
data_string = f"nama = {nama}, umur = {umur}, tinggi = {tinggi}, no sepatu = {no_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

#string Multiline
data_string = f"nama = {nama},\n umur = {umur},\n tinggi = {tinggi},\n no sepatu = {no_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""nama = {nama}
umur = {umur}
tinggi = {tinggi}
no sepatu = {no_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

#mengatur lebar
data_string = f"""
nama    = {nama:}
umur    = {umur:>5}
tinggi  = {tinggi:}
sepatu  = {no_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)