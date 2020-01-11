f = open("file", "rb")

b = list(f.read())
b = list(map(lambda x: hex(x), b))

print(b)