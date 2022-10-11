from time import sleep

import lecture_fichier_challenge as lfc
import list_challenge as lch
import functions_challenge as fc
import dictionnary as dtv
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
    exit_app = "exit app"

    questions = [
      inquirer.List('challenge',
                    message="What challenge you desire ?",
                    choices=[read_files, house_price, function_challenge, dictionary_challenge, data_frame, data_data, numpy, exit_app],
                ),
    ]
    answers = inquirer.prompt(questions)

    print(answers["challenge"])

    if answers["challenge"] == read_files:
        lfc.read_files()

    if answers["challenge"] == house_price:
        lch.house_price()

    if answers["challenge"] == function_challenge:
        fc.functions_challenge()

    if answers["challenge"] == dictionary_challenge:
        dtv.dictionary_challenge()

    if answers["challenge"] == exit_app:
        print("Thanks for you're visite. Have a good day.")
        exit()

    questions = [
        inquirer.Confirm("continue", message="Should I continue"),
    ]

    answers = inquirer.prompt(questions)

    if answers["continue"] == True:
        choice_challenge()
    else:
        print("Thanks for you're visite. Have a good day.")


choice_challenge()




