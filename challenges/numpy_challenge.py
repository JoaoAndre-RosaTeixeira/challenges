import numpy as numpy
import pandas as pd


def start():
    df_marathon = pd.read_csv("ressource/numpy/marathon.txt", delimiter="\t",
                              names=["city", "year", "hour", "secondes"])

    paris = []
    berlin = []

    for i, data in df_marathon["city"].items():
        if data == "PARIS":
            paris.append(1)
        else:
            paris.append(0)
        if data == "BERLIN":
            berlin.append(1)
        else:
            berlin.append(0)
    df_marathon["estPARIS"] = paris
    df_marathon["estBERLIN"] = berlin

    Y = df_marathon["secondes"].to_numpy()
    X = df_marathon[["year", "estPARIS", "estBERLIN"]].to_numpy()

    XT = X.T
    XX = numpy.dot(XT, X)
    XXT = numpy.linalg.inv(XX)
    XXT_XP = numpy.dot(XXT, XT)
    A = numpy.dot(XXT_XP, Y)

    print(f"Aa est égale à {A[0]}.")
    print(f"A1 est égale à {A[1]}.")
    print(f"A2 est égale à {A[2]}.")
