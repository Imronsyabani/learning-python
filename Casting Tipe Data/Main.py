# Casting:  merubah 1 tipe data ke tipe data yang lain 
#tipe data: int,float,string,bool
#INTEGER
print("=====INTEGER=====")
data_int = 10
print("data = ",data_int,", type = ",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ",data_float,", type = ",type(data_float))
print("data = ",data_str,", type = ",type(data_str))
print("data = ",data_bool,", type = ",type(data_bool))

#FLOAT
print("=====FLOAT=====")
data_float = 9.5
print("data = ",data_float,", type = ",type(data_float))

data_int = int(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ",data_int,", type = ",type(data_int))
print("data = ",data_str,", type = ",type(data_str))
print("data = ",data_bool,", type = ",type(data_bool))

#FLOAT
print("=====BOOLEAN=====")
data_bool = False;
print("data = ",data_bool,", type = ",type(data_bool))

data_int = int(data_bool) #akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool) #akan false jika nilai float
print("data = ",data_int,", type = ",type(data_int))
print("data = ",data_str,", type = ",type(data_str))
print("data = ",data_float,", type = ",type(data_float))