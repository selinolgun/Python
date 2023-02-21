names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998, 2000, 1998, 1987]

names.append("Cenk")
print(names)

names.insert(0, "Sena")
print(names)

# names.remove("Deniz")
# print(names)

index = names.index("Deniz")
print(index)

result = "Ali" in names
print(result)

names.reverse()
print(names)

names.sort()
print(names)

years.sort()
print(years)

str = "Chevrolet,Dacia"
result = str.split(",")
print(result)

years.sort()
print(years[0])
print(years[3])
min = min(years)
max = max(years)
print(min, max)

x = years.count(1998)
print(x)

years.clear()
print(years)

marka1 = [input("1. Marka:")]
marka2 = [input("2. Marka:")]
marka3 = [input("3. Marka:")]
y = [marka1, marka2, marka3]
print(y)