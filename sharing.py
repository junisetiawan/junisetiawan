#program membuat bentuk segitiga biasa dan segitiga siku siku 
n = int(input("masukan tinggi segitiga : "))
print()

for i in range(n):
    for j in range(n,i,-1):
        print("_",end = "")
    for j in range(2*i+1):
        print("*",end = "")
    print()        
#untuk variabel tiggi line 12 bisa di ganti sesuai masukan
Tinggi = 10
for i in range (1, Tinggi+1):
    print(i*"* ")    