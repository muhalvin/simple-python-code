numb = input("Masukkan angka: ")

pola = {
    '0': [
        '*****  ',
        '*   *  ',
        '*   *  ',
        '*   *  ',
        '*****  ',
    ],
    '1': [
        '    *  ',
        '    *  ',
        '    *  ',
        '    *  ',
        '    *  ',
    ],
    '2': [
        '*****  ',
        '    *  ',
        '*****  ',
        '*      ',
        '*****  ',
    ],
    '3': [
        '*****  ',
        '    *  ',
        '*****  ',
        '    *  ',
        '*****  ',
    ],
    '4': [
        '*   *  ',
        '*   *  ',
        '*****  ',
        '    *  ',
        '    *  ',
    ],
    '5': [
        '*****  ',
        '*      ',
        '*****  ',
        '    *  ',
        '*****  ',
    ],
    '6': [
        '*****  ',
        '*      ',
        '*****  ',
        '*   *  ',
        '*****  ',
    ],
    '7': [
        '*****  ',
        '    *  ',
        '    *  ',
        '    *  ',
        '    *  ',
    ],
    '8': [
        '*****  ',
        '*   *  ',
        '*****  ',
        '*   *  ',
        '*****  ',
    ],
    '9': [
        '*****  ',
        '*   *  ',
        '*****  ',
        '    *  ',
        '*****  ',
    ]
}

def print_pola(pola):
    for baris in pola:
        print(baris)
        
# Function untuk cetak pola
for digit in numb:
    if digit in pola:
        print_pola(pola[digit])
        print("\n")
    else:
        print(digit, ": Bukan Angka.")