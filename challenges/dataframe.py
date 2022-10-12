import pandas as pd


def dataframe_f():
    df_google_ap_1 = pd.read_csv("ressource\dataframe_challenge\googleplaystore_1.csv", sep=";")

    df_milliards = df_google_ap_1[df_google_ap_1['Installs'].str.contains('1,000,000,000+')]
    print(df_milliards[["App", "Category", "Genres"]])

    df_max = df_google_ap_1[df_google_ap_1['Reviews'] == df_google_ap_1['Reviews'].max()]
    print(df_max[["App", "Category", "Genres"]])

    print(df_google_ap_1.iloc[3:17 , [2, 5, 6]])

    len_app_everyone = len(df_google_ap_1[df_google_ap_1['Content Rating'].str.contains('Everyone')])
    print(f"Il y a {len_app_everyone} applications ouvertes aux personnes de tout âges")

    categorys = []
    actual_category = ""
    for category in df_google_ap_1['Category']:
        if actual_category != category:
            actual_category = category
            categorys.append(category)

    actual_len = 0
    category_name = ""
    for category in categorys:
        if actual_len < len(df_google_ap_1[df_google_ap_1['Category'].str.contains(category)]):
            actual_len = len(df_google_ap_1[df_google_ap_1['Category'].str.contains(category)])
            category_name = category
    print(f"La categorie avec le plus d'applications est {category_name} avec pas moins de {actual_len} applications.")


    def convert_max_price(price):
        return float(price.replace("$", "").replace("Free", "0"))



    max_price = 0
    max_price_data = ""
    for data in df_google_ap_1['Price']:
        actual_price = convert_max_price(data)
        if max_price < actual_price:
            max_price = actual_price
            max_price_data = data
    df_price = df_google_ap_1[df_google_ap_1['Price'] == max_price_data]
    res = df_price["App"].values[0]
    print(f"l'application qui a le prix le plus chere est {res}.")


