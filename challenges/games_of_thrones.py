import inquirer
import pandas as pd

def start():
    max_len = 0
    dictionnaire_bien_choisi = {
        "words": {'eddard', 'catelyn', 'robb', 'sansa', 'arya', 'brandon',
                  'rickon', 'theon', 'rorbert', 'cersei', 'tywin', 'jaime',
                  'tyrion', 'shae', 'bronn', 'lancel', 'joffrey', 'sandor',
                  'varys', 'renly', 'a'}
    }



    # fonction pour rechercher le mot selon la position de la lettre
    def mots_lettre_position(liste, lettre, position):
        list_word = []
        for word in liste:
            if len(word) >= position:
                if word[position - 1] == lettre:
                    list_word.append(word)
        return list_word

    # permet de choisir dans le terminal qu'elle lettre ont desire
    # avec condition afin d'eviter les erreurs de saisie
    def selection_letter():
        questions = [
            inquirer.Confirm("selection_letter", message="enter the letter to reseacrh ?(base letter 'y' it's defined)", default=True),
        ]
        answers = inquirer.prompt(questions)

        if answers["selection_letter"] == True:

            while True:
                user_input = input('Enter letter(letter only): ')

                if not user_input.isalpha() or len(user_input) > 1:
                    print('Enter only one letter')
                    continue
                else:
                    return user_input


    letter_find = selection_letter()
    if letter_find == None:
        letter_find = "y"
    # permet d'ajouter un nouveau mot au dictrionnaire
    def new_word():
        questions = [
            inquirer.Confirm("new_word", message="Who wish add a new word ?", default=True),
        ]
        answers = inquirer.prompt(questions)
        user_input = False

        if answers["new_word"] == True:


            while True:
                user_input = input('Enter new word(letters only): ')


                if not user_input.isalpha():
                    print('Enter only letters')
                    continue
                else:
                    break
        pf = pd.read_csv("words.csv")
        if user_input != False:
            new_row = {'words': user_input}
            pf = pf.append(new_row, ignore_index=True)
            pf.to_csv("words.csv")
        for i, word in pf['words'].items():
            print(word, "obiwan fuckkin kenobi")

            dictionnaire_bien_choisi["words"].add(word)
    new_word()

    print(dictionnaire_bien_choisi["words"])
    for word in dictionnaire_bien_choisi["words"]:
        print(word)
        if len(word) > max_len:
            max_len = len(word)
    choose_position = [*range(1, max_len + 1)]

    questions = [
        inquirer.List('position',
                      message="What position you desire ?",
                      choices=choose_position,
                      ),
    ]

    answers = inquirer.prompt(questions)

    print(mots_lettre_position(dictionnaire_bien_choisi["words"], letter_find, answers["position"]))

