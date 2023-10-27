total_harga = 0

topping = input("Masukkan topping yang diinginkan: ")

if topping == "frankfurter bbq" or topping == "meat monsta" or topping == "super supreme" or topping == "super supreme chicken" or topping == "meat lovers" or topping == "chicken lovers" or topping == "cheese lovers" or topping == "american favourite":
    total_harga = 50000
else:
    total_harga = 0
    print("Maaf, topping pizza yang anda masukkan tidak tersedia")

CrustPizza = input("Masukkan crust pizza yang diinginkan: ")
if CrustPizza == "original" :
    total_harga += 0
elif CrustPizza == "StuffedCrust Cheese" :
    total_harga += 20000
elif CrustPizza == "StuffedCrust Sausage" :
    total_harga += 10000
elif CrustPizza == "CheesyBites" :
    total_harga += 5000
else:
    print("Maaf, Crust Pizza yang anda masukkan tidak tersedia")

ukuran = input("Masukkan ukuran pizza yang diinginkan: ")
if ukuran == "Regular" :
    total_harga += 0
elif ukuran == "Medium" :
    total_harga += 20000
elif ukuran == "Large" :
    total_harga += 40000
else:
    print("Maaf, ukuran pizza yang anda masukkan tidak tersedia")

chese = input("ingin tambah keju? (y/n): ")
if chese == "y" :
    total_harga += 13000
elif chese == "n" :
    total_harga += 0
else:
    print("Maaf, pilihan anda tidak tersedia")

print("Total harga: Rp",total_harga)