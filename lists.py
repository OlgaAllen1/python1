name = "Olga"
names = ['olga', 'Leon', 'Elizabeth']
print(names)
print(names[1])
names[1] = "leon"
print(names[1])
names.sort()
print(names)
names.append("Nadezhda")
print(names)
print(len(names))
print(names.index("leon"))
for name in names:
    print("Hello"+" "+name)
