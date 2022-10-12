def functions_challenge():

    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(myList)
    myList.sort()
    print(myList)


    # median for myList
    def median_f(list):
        if n % 2 == 0:
            median1 = list[n // 2]
            median2 = list[n // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = list[n // 2]
        return median


    # somme of myList
    def sum_list_f(list):
        listSum = sum(list)
        return listSum

    # moyenne of myList
    def mean_list_f(list):
        moyenne_list = sum_list_f(list) / len(list)
        return moyenne_list


    # variance de myList
    def variance_list_f(list):
        variance_list = []
        for num in list:
            variance_list.append((num - mean_list_f(list)) ** 2)
        variance = sum(variance_list) / len(variance_list)
        return variance

    # ecart type of myList
    def ecart_type_list_f(list):
        ecart_type = pow(variance_list_f(list), 0.5)
        return ecart_type


    print(f"la median de my_list est {median_f(myList)}")
    print(f"la somme de my_list est {sum_list_f(myList)}")
    print(f"la moyenne de my_list est {mean_list_f(myList)}")
    print(f"la variance de my_list est {variance_list_f(myList)}")
    print(f"l'ecart type de my_list est {ecart_type_list_f(myList)}")

