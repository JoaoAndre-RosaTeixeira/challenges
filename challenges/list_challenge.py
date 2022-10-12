import random

def house_price():
    list_house = [*range(0, 58)]
    prix_de_58_maisons = []
    for i in list_house:
        prix_de_58_maisons.append(random.randint(125000, 700000))

    print(prix_de_58_maisons)


    price_1 = 0
    price_2 = 0
    price_3 = 0
    price_4 = 0
    for i in prix_de_58_maisons:
        if i >= 300000:
            price_1 += 1
        if 250000 < i < 400000:
            price_2 += 1
        if i < 600000:
            price_3 += 1
        if i < 150000 or i > 650000:
            price_4 += 1
    print(f"il y a {price_1} maisons dont le prix est supérieur ou egal à 300 000€")
    print(f"il y a {price_2} maisons dont le prix est compris entre 250 000€ et 400 000€")
    print(f"il y a {price_3} maisons dont le prix n'est pas supérieur à 600 000€")
    print(f"il y a {price_4} maisons dont le prix est inférieur à 150 000€ ou supérieur à 650 000€")

