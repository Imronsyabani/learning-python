# a = 10, a adalah variabel dan 10 adalah value

#tipe data: Angka satuan yang tidak ada koma / integer
data_integer = 1
print("data:",data_integer)
print("Bertipe:",type(data_integer))

#tipe data: angka dengan koma (float)
data_float = 1.1
print("data:",data_float)
print("Bertipe:",type(data_float))

#tipe data: kumpulan karakter (string)
data_string = "imron syabani"
print("data:",data_string)
print("Bertipe:",type(data_string))

#tipe data: biner true/false (boolean)
data_bool = True
print("data:",data_bool)
print("Bertipe:",type(data_bool))

#tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data:",data_complex)
print("Bertipe:",type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data:",data_c_double)
print("Bertipe:",type(data_c_double))