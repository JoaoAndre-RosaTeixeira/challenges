import inquirer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def data_f():
    df_erp = pd.read_excel('ressource/challenge_data/erp.xlsx')
    df_web = pd.read_excel('ressource/challenge_data/web.xlsx')
    df_liaison = pd.read_excel('ressource/challenge_data/liaison.xlsx')

    df_web = df_web[df_web["post_mime_type"] != "image/jpeg"]

    df_erp = df_erp.merge(df_liaison, left_on='product_id', right_on='product_id', how="right")
    df_marchand = df_erp.merge(df_web, left_on='id_web', right_on='sku', how="left")

    df_marchand = df_marchand[df_marchand['sku'].notna()]

    df_marchand.to_csv("df_marchand.csv")

    somme = 0
    products_sum = {"name": {}, "sum_revenue": {}}

    # ajoute a product sum le nom et les revenue par produit
    for i, data in df_marchand['price'].items():
        products_sum["name"][i] = df_marchand['post_title'][i]
        res = data * df_marchand['total_sales'][i]
        products_sum["sum_revenue"][i] = res
        somme += res

    print_products_sum = "chiffre d'affaire par produit."
    print_sell_sum = "chiffre d'affaire total"
    print_graph_of_zscore = "afficher le graphique des aberration des prix par rapport au z score"
    exit_app = "exit data challenge"

    # navigation dans le terminal
    def choose():
        questions = [
            inquirer.List('choose',
                          message="What challenge you desire ?",
                          choices=[print_products_sum, print_sell_sum, print_graph_of_zscore, exit_app],
                          ),
        ]
        answers = inquirer.prompt(questions)

        print(answers["choose"])

        if answers["choose"] == print_products_sum:
            products_sum_f()

        if answers["choose"] == print_sell_sum:
            sell_sum_f()

        if answers["choose"] == print_graph_of_zscore:
            graph_of_zscore_f()

        if answers["choose"] == exit_app:
            print("Thanks for you're visite. Have a good day.")
            return
        else:
            choose()

    # affiche le chiffre d'affaire de chaque produits
    def products_sum_f():
        print(f"les produits et leurs chiffre d'affaire : ")
        for i, str in products_sum['name'].items():
            print(f"name : {products_sum['name'][i]}")
            print(f"chiffres d'affaires : {products_sum['sum_revenue'][i]}")

    # affiche le chiffre d'affaier total
    def sell_sum_f():
        print(f"le total du chiffre d'affaire est de {somme}")

    # fonction creation des graphique
    def graph_of_zscore_f():
        print(f"Close window of zscore graph for continue programme")

        mean = np.mean(df_marchand['price'])
        std = np.std(df_marchand['price'])

        # creation d'une nouvelle dataframe et ajout de la colone zscore
        df_zscore = df_marchand[["post_title", 'price']]
        df_zscore.reset_index(inplace=True)
        z_score_col = []
        for i, data in df_zscore['price'].items():
            z = (data - mean) / std
            z_score_col.append(z)

        df_zscore['z_score'] = z_score_col

        # création des deux graphiques en utilisant matplotlib
        plt.figure(figsize=(14, 8))
        plt.subplot(1, 2, 1)
        s = [7 * 4 ** n for n in range(len(df_zscore['price']))]
        plt.scatter(df_zscore.index, df_zscore['price'], c=df_zscore["z_score"])

        plt.xlabel("number products")
        plt.ylabel("price")

        plt.title("Outlier by Z score")
        plt.subplot(1, 2, 2)
        plt.boxplot(df_zscore['price'], flierprops=dict(markerfacecolor='y', marker='*'))

        plt.show()

    choose()
