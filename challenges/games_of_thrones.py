import inquirer


def start():
    max_len = 0
    dictionnaire_bien_choisi = {
        "words": {'eddard', 'catelyn', 'robb', 'sansa', 'arya', 'brandon',
                  'rickon', 'theon', 'rorbert', 'cersei', 'tywin', 'jaime',
                  'tyrion', 'shae', 'bronn', 'lancel', 'joffrey', 'sandor',
                  'varys', 'renly', 'a'}
    }

    letter_find = "y"


    def mots_lettre_position(liste, lettre, position):
        list_word = []
        for word in liste:
            if len(word) >= position:
                if word[position - 1] == lettre:
                    list_word.append(word)
        return list_word


    def selection_letter():
        questions = [
            inquirer.Confirm("selection_letter", message="enter the letter to reseacrh :", default=True),
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


    def new_word():
        questions = [
            inquirer.Confirm("new_word", message="Who wish add a new word ?", default=True),
        ]
        answers = inquirer.prompt(questions)

        if answers["new_word"] == True:
            user_input = ''

            while True:
                user_input = input('Enter new word(letters only): ')

                if not user_input.isalpha():
                    print('Enter only letters')
                    continue
                else:
                    dictionnaire_bien_choisi["words"].add(user_input)
                    break
    new_word()


    for word in dictionnaire_bien_choisi["words"]:
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

