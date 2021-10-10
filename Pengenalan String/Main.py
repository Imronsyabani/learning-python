# cara membuat string

data = "ini adalah string"
print(data)
print(type(data))

'''
     1. membuat string dengan quote '...' , "...."
'''
strSingleQuote = 'ini menggunakan single quote'
print(strSingleQuote)

strDoubleQuote = "ini menggunakan double quote"
print(strDoubleQuote)

# 2 menggunakan tanda khusus seperti backslash \
print('ini adalah hari jum\'at')
print('g\'day, isn\'t, it?')

print("C:users\imron\syabani")

# karakter khusus

# tab
print("imron\t\t\tsyabani")

#backspace
print("imron\bsyabani")

# newline
print("baris pertama. \nbaris kedua.") # LF => Line Feed -> biasa digunakan oleh unix,linux,macos
print("baris pertama. \rbaris kedua.") # CR => Carriage Return -> biasa digunakan oleh commode, acorn, lisp
print("baris pertama. \r\nbaris kedua.") # CRLF => Line Feed Carriage Return -> biasa digunakan oleh windows

# 3. string literal atau raw
# raw string 
print(r'C:\\Users\Imron Syabani')

# MultiLine literal string 
print("""
nama:Imron Syabani
umur: 19
status:lajang
""")

# multiline literal string dan raw
print(r"""
Nama: Imron Syabani
Asal Sekolah: SMK Islamiyah TKJ Ciputat
Hobby: Main Game dan Programming
""")