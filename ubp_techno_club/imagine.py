"""
Menyeberangi Jembatan Gantung

Setelah membantu penduduk dengan makanan, mereka mengizinkanmu melintasi jembatan gantung. 
Namun, jembatan ini sangat rapuh. Hanya orang-orang dengan berat badan tertentu yang boleh menyeberang. 
Kamu harus menulis program untuk menentukan apakah kamu bisa menyeberang jembatan.

Contoh 1
Input:
weight = 50

Output:
Kamu tidak boleh menyeberang jembatan

Contoh 2
Input:
weight = 90

Output:
Kamu boleh menyeberang jembatan
"""
# Input berat badan dari pengguna
weight = int(input("Weight: "))  # Pastikan untuk mengonversi input ke integer

# Tentukan batas minimum dan maksimum berat yang diizinkan
min_weight = 80
max_weight = 100

# Periksa apakah berat memenuhi syarat
if min_weight <= weight <= max_weight:
    print("Kamu boleh menyeberang jembatan")
else:
    print("Kamu tidak boleh menyeberang jembatan")
