def avg_words(s1):
    a = len(s1.split(' '))
    b = len(s1.split('.')) - 1
    avg = a / b
    print("Среднее количество слов в предложении " + str(avg))
def create_dict(s1):
    mas = []
    dict = {}
    st = ""
    for i in s1:
        if i == ' ' or i == '.':
            if st != '':
                mas.append(st)
            st = ""
        else:
            st += i

    for i in mas:
        dict[i] = mas.count(i)
    for k, v in dict.items():
        print(str(k) + " : " + str(v))
def sort_dict(s1):
    mas = []
    dict = {}
    str = ""
    for i in s1:
        if i == ' ' or i == '.':
            if str != '':
                mas.append(str)
            str = ""
        else:
            str += i

    for i in mas:
        dict[i] = mas.count(i)
    lis = sorted(dict.items(), key=lambda x: x[1])
    dict = dict(lis)
    print(dict)
s1 = input("Введите текст ")
while(1):

    print("\n1:Вывести среднее количество слов")
    print("2:Вывести сколько раз встречается каждое слово")
    print("3:Вывести отсортировать список слов")
    print("Введите любое другое число если хотите выйти")
    c = input("Введите что вы хотите сделать> ")
    if c == '1':
        avg_words(s1)
    elif c == '2':
        create_dict(s1)
    elif c =='3':
        sort_dict(s1)
    else:
        print("Всего хорошего!")
        break



