tahun = int(input('Masukan Tahun : '))
if tahun % 400 == 0:
    print("Tahun",tahun,"merupakan Tahun Kabisat")
elif tahun % 4 == 0 and tahun % 100 != 0:
    print("Tahun",tahun,"merupakan Tahun Kabisat")
else:
    print("Tahun",tahun,"Bukan Tahun Kabisat")