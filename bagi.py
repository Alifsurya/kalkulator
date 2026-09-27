def bagi(angka1, angka2):
    if angka2 == 0 or angka1 == 0:
        raise ValueError("Tidak bisa dibagi dengan nol.")
    return angka1 / angka2