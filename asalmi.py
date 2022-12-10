a=int(input("bir sayı gir:"))
asalmidir=True

if a<=1:
    asalmidir=False

for t in range(2,a):
    if(a%t==0):
        asalmidir=False
        break


if asalmidir:
    print("sayı asaldır ")
else:
    print("sayı asal değildir ")    


