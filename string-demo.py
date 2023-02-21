website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

print(len(course))
print(website[7:10])
print(website[22:])
print(course[:50])
print(course[50:])
# print((course)) tersten
print(course[::-1])

name = "Bora"
surname = "Yılmaz"
age = 32
job = "mühendis"

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

# harf değiştirme
b = "Hello world"
# print(b[6])
b = b[0:6] + "W" + b[-4:]
print(b)
b.replace("w", "W")
print(b)

a = "abc"
print(a + a + a)
