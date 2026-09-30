nilai = float(input("Nilai 1-100: "))
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 1-100: "))
print(f"Nilai diterima: {nilai}")