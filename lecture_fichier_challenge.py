import pandas as pd
from simpledbf import Dbf5


def read_files():
    dbf = Dbf5('ressource\mar2012.dbf')
    df_dbf = dbf.to_dataframe()

    data_csv = pd.read_csv("ressource\mar2012.csv", low_memory=False)
    df_csv = pd.DataFrame(data_csv)

    data_txt = pd.read_csv('ressource\prima.txt', delimiter="\t")
    df_txt = pd.DataFrame(data_txt)

    # output the dataframe
    print(df_dbf)
    print(df_csv)
    print(df_txt)
