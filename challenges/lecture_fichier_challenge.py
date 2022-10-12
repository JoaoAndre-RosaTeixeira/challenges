import pandas as pd
from simpledbf import Dbf5
import warnings
warnings.simplefilter("ignore")


def read_files():
    dbf = Dbf5('ressource/read_files_challenge/mar2012.dbf')
    df_dbf = dbf.to_dataframe()

    data_csv = pd.read_csv("ressource/read_files_challenge/mar2012.csv", low_memory=False)
    df_csv = pd.DataFrame(data_csv)

    data_txt = pd.read_csv('ressource/read_files_challenge/prima.txt', delimiter="\t")
    df_txt = pd.DataFrame(data_txt)

    # output the dataframe_challenge
    print(df_dbf)
    print(df_csv)
    print(df_txt)
