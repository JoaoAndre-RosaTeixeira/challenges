from challenges import lecture_fichier_challenge as lfc, functions_challenge as fc, dataframe as dtf, \
    list_challenge as lch, dictionnary as dtv
from challenges import data as dt
from challenges import games_of_thrones as got
from challenges import numpy_challenge as nmy
import inquirer


# WARNING !! Use command "python main.py" to run this code
def choice_challenge():
    read_files = 'lecture de fichier'
    house_price = 'house price list challenge'
    function_challenge = 'functions challenge(median, somme, moyenne, variance, ecart type)'
    dictionary_challenge = 'Dictionnaire des vendeurs '
    data_frame = 'Dataframe'
    data_data = 'Data'
    numpy = 'Numpy'
    games_of_thrones = "games of thrones"
    exit_app = "exit app"

    questions = [
        inquirer.List('challenge',
                      message="What challenge you desire ?",
                      choices=[read_files, house_price, function_challenge, dictionary_challenge, data_frame, data_data,
                               numpy, games_of_thrones, exit_app],
                      ),
    ]
    answers = inquirer.prompt(questions)

    print(f"You have selected {answers['challenge']}")

    if answers["challenge"] == read_files:
        lfc.read_files()

    if answers["challenge"] == house_price:
        lch.house_price()

    if answers["challenge"] == function_challenge:
        fc.functions_challenge()

    if answers["challenge"] == dictionary_challenge:
        dtv.dictionary_challenge()

    if answers["challenge"] == data_frame:
        dtf.dataframe_f()

    if answers["challenge"] == data_data:
        dt.data_f()

    if answers["challenge"] == games_of_thrones:
        got.start()

    if answers["challenge"] == numpy:
        nmy.start()

    if answers["challenge"] == exit_app:
        print("Thanks for your visit. Have a nice day.")
        exit()

    questions = [
        inquirer.Confirm("continue", message="Should I continue ?(yes = go Home selection, No = close app)",
                         default=True),
    ]

    answers = inquirer.prompt(questions)

    if answers["continue"] == True:
        choice_challenge()
    else:
        print("Thanks for you're visite. Have a good day.")


choice_challenge()
