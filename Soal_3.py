barang = int(input('Masukan Jumlah Barang : '))
total = 0
for i in range(barang):
    harga = int(input(f'Masukan harga barang {i + 1} : '))
    total += harga
print('Total Belanjaan : Rp.',total)