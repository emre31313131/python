f = open("data", "r")

zort= f.read().split("\n")

dictionary= {}
for a in zort:
    key, value = a.split(": ")
    dictionary[key] = value

print(dictionary)
f.close()

