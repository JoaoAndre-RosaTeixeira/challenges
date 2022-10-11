import pandas as pd
def dataframe_f():
    data_google_ap_1 = pd.read_csv("ressource\googleplaystore_1.csv", on_bad_lines='skip')
    df_google_ap_1 = pd.DataFrame(data_google_ap_1,
                                  columns=['name', 'category', 'rating', 'reviews', 'size', 'installs', 'type', 'price',
                                           'content_rating', 'genres', 'last_update', 'current_ver', 'android_ver'])

    df_google_ap_1.reset_index()

    for data in data_google_ap_1.columns:
        print(data)


    # i = 0
    #
    # for data in data_google_ap_1:
    #
    #     print(data["installs"])
    #     print("/n")
    #
    #     if data == "Installs":
    #         print(data, "hello there")
    #
    #     if data == "Installs":
    #         for x in data:
    #             if x >= 1000000000:
    #                 print(df_google_ap_1.columns["App"][i])
    #     i+=1

    # print(data, "hello there. is this fucking obiwan kenobi")
    # print(data['Installs'].unique())
    #
    # if int(data['Installs']) >= 1000000000:
    #     print(data['App'], data['Category'], data['Genres'])


dataframe_f()
