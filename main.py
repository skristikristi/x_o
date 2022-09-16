lentele = [1, 2, 3,
           4, 5, 6,
           7, 8, 9]


def spausdinti_lentele():
    print(lentele[0], '|', lentele[1], '|', lentele[2])
    print('---------')
    print(lentele[3], '|', lentele[4], '|', lentele[5])
    print('---------')
    print(lentele[6], '|', lentele[7], '|', lentele[8])


print(spausdinti_lentele())
count = 0

while True:
    while True:
        try:
            skaicius = int(input("X: pasirinkite skaičių: "))
            lentele = ['X' if elementas == skaicius else elementas for elementas in lentele]
            break
        except ValueError:
            print("Įvedėte ne skaičių. Bandykite dar kartą")
            print(spausdinti_lentele())
    if lentele[0] == lentele[1] == lentele[2] == 'X':
        print("Pirmasis žaidėjas laimėjo!")
        break
    elif lentele[3] == lentele[4] == lentele[5] == 'X':
        print("Pirmasis žaidėjas laimėjo!")
        break
    elif lentele[6] == lentele[7] == lentele[8] == 'X':
        print("Pirmasis žaidėjas laimėjo!")
        break
    elif lentele[0] == lentele[3] == lentele[6] == 'X':
        print("Pirmasis žaidėjas laimėjo")
        break
    elif lentele[1] == lentele[4] == lentele[7] == 'X':
        print("Pirmasis žaidėjas laimėjo!")
        break
    elif lentele[2] == lentele[5] == lentele[8] == 'X':
        print("Pirmasis žaidėjas laimėjo!")
        break
    elif lentele[0] == lentele[4] == lentele[8] == 'X':
        print("Pirmasis žaidėjas laimėjo!")
        break
    elif lentele[2] == lentele[4] == lentele[6] == 'X':
        print("Pirmasis žaidėjas laimėjo")
        break

    print(spausdinti_lentele())
    count += 1
    if count == 5:
        print("Žaidimas baigtas, laimėtojų nėra.")
        break
    while True:
        try:
            skaicius = int(input("O: pasirinkite skaičių: "))
            lentele = ['O' if elementas == skaicius else elementas for elementas in lentele]
            break
        except ValueError:
            print("Įvedėte ne skaičių. Bandykite dar kartą")
            print(spausdinti_lentele())
    if lentele[0] == lentele[1] == lentele[2] == 'O':
        print("Antrasis žaidėjas laimėjo!")
        break
    elif lentele[3] == lentele[4] == lentele[5] == 'O':
        print("Antrasis žaidėjas laimėjo!")
        break
    elif lentele[6] == lentele[7] == lentele[8] == 'O':
        print("Antrasis žaidėjas laimėjo!")
        break
    elif lentele[0] == lentele[3] == lentele[6] == 'O':
        print("Antrasis žaidėjas laimėjo!")
        break
    elif lentele[1] == lentele[4] == lentele[7] == 'O':
        print("Antrasis žaidėjas laimėjo!")
        break
    elif lentele[2] == lentele[5] == lentele[8] == 'O':
        print("Antrasis žaidėjas laimėjo!")
        break
    elif lentele[0] == lentele[4] == lentele[8] == 'O':
        print("Antrasis žaidėjas laimėjo!")
        break
    elif lentele[2] == lentele[4] == lentele[6] == 'O':
        print("Antrasis žaidėjas laimėjo!")
        break
    print(spausdinti_lentele())
