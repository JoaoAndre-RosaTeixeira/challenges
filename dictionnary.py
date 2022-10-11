# premier systeme de rangement je voulais le faire sous une list contenant des dict
# mais je me suis arretez a ca pour essayer
# ventes_commerciaux = [
#     {
#         "name": "Marie",
#         "vente": 15
#     },
#     {
#         "name": "Samuel",
#         "vente": 17
#     },
#     {
#         "name": "Gaston",
#         "vente": 12
#     },
#     {
#         "name": "Fred",
#         "vente": 10
#     },
#     {
#         "name": "Mae",
#         "vente": 5
#     },
#     {
#         "name": "Julie",
#         "vente": 15
#     },
#     {
#         "name": "Zoe",
#         "vente": 7
#     },
#     {
#         "name": "Claire",
#         "vente": 20
#     },
#     {
#         "name": "Chloe",
#         "vente": 8
#     },
#     {
#         "name": "Julien",
#         "vente": 14
#     },
#     {
#         "name": "Gael",
#         "vente": 9
#     },
#     {
#         "name": "Samia",
#         "vente": 15
#     },
#     {
#         "name": "Omar",
#         "vente": 11
#     },
#     {
#         "name": "Gabriel",
#         "vente": 16
#     },
#     {
#         "name": "Manon",
#         "vente": 2
#     }
# ]
#
#
# for p_id, p_info in ventes_commerciaux.items():
#     print(ventes_commerciaux[p_id]["vente"])
from statistics import mean


def dictionary_challenge():
    ventes_commerciaux = {
        "name": [
            "Marie",
            "Samuel",
            "Gaston",
            "Fred",
            "Mae",
            "Julie",
            "Zoe",
            "Claire",
            "Chloe",
            "Julien",
            "Gael",
            "Samia",
            "Omar",
            "Gabriel",
            "Manon"
        ],
        "ventes": [
            15,
            17,
            12,
            10,
            5,
            15,
            7,
            20,
            8,
            14,
            9,
            15,
            11,
            16,
            2
        ]
    }

    def mean_ventes():
        return mean(ventes_commerciaux['ventes'])

    print(f"La moyenne de vente est de {mean_ventes()}")
    print(f"Il y a {len(ventes_commerciaux['name'])} vendeurs")

    commerciaux_have_mean = 0
    commerciaux_have_long_name = 0
    best_vendeur_key = 0
    best_sell = 0
    selling_pair_key = []
    for id, values in ventes_commerciaux.items():
        if id == 'ventes':
            for x in values:
                if x > mean_ventes():
                    commerciaux_have_mean += 1
                if x > best_sell:
                    best_sell = x
                    best_vendeur_key = values.index(x)
                if  x % 2 == 0:
                    selling_pair_key.append(values.index(x))
        if id == 'name':
            for x in values:
                if len(x) < 4:
                    commerciaux_have_long_name += 1
    selling_pair = []
    for data in selling_pair_key:
        selling_pair.append(ventes_commerciaux['name'][data])


    print(f"Il y a {commerciaux_have_mean} vendeurs qui vendent plus que la moyenne")
    print(f"{ventes_commerciaux['name'][best_vendeur_key]} est le meilleur vendeur avec {ventes_commerciaux['ventes'][best_vendeur_key]} ventes")
    print(f"Il y a {commerciaux_have_long_name} vendeurs qui ont un prénom qui ont moins de 4 lettres")
    print(f"les vendeurs avec des ventes pair sont {selling_pair}")
