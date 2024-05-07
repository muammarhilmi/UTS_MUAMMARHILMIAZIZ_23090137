def hitung():
    berat = int(input('Masukkan Berat Badan (Kg): '))
    tinggi = float(input('Masukkan Tinggi Badan (M): '))
    bmi = berat / (tinggi ** 2)
    print('Berat Badan : ',berat)
    print('Tinggi Badan : ', tinggi)
    print('Nilai BMI Anda :',bmi)
    if bmi < 18.5:
        print('Kategori BMI : Berat Badan Kurang')
    elif 18.5<=bmi<24.9:
        print('Kategori BMI: Berat Badan Normal')
    elif 25<=bmi<29.9:
        print('Kategori BMI: Kelebihan Berat Badan')
    elif bmi>=30:
        print('Kategori BMI : Obesitas')