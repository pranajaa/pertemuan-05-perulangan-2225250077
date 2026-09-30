n = int(input("n: "))
jumlah_genap = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1
print(f"Bilangan genap = {jumlah_genap}")