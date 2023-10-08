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

font_size = int(input("Masukkan ukuran font (1-10): "))

def scale_pattern(pattern, size):
    scaled_pattern = []
    for line in pattern:
        scaled_line = ""
        for char in line:
            if char == '*':
                scaled_line += '*' * size
            else:
                scaled_line += ' ' * size
        scaled_pattern.extend([scaled_line] * size)
    return scaled_pattern

for digit in numb:
    if digit in pola:
        scaled_pattern = scale_pattern(pola[digit], font_size)
        for line in scaled_pattern:
            print(line)
        print("\n")
    else:
        print(digit, ": Bukan Angka.")
