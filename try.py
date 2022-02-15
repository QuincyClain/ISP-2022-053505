def avg_slov(s1):
    a = len(s1.split(' '))
    b = len(s1.split('.')) - 1
    avg = a / b
    print("Среднее количество слов в предложении " + str(avg))
def create_dict(s1):
    xz = []
    dic = {}
    st = ""
    for i in s1:
        if i == ' ' or i == '.':
            if st != '':
                xz.append(st)
            st = ""
        else:
            st += i

    for i in xz:
        dic[i] = xz.count(i)
    for k, v in dic.items():
        print(str(k) + " : " + str(v))
def sort_dict(s1):
    xz = []
    dic = {}
    str = ""
    for i in s1:
        if i == ' ' or i == '.':
            if str != '':
                xz.append(str)
            str = ""
        else:
            str += i

    for i in xz:
        dic[i] = xz.count(i)
    lis = sorted(dic.items(), key=lambda x: x[1])
    dic = dict(lis)
    print(dic)
s1 = input("Введите текст ")
while(1):

    print("\n1:Вывести среднее количество слов")
    print("2:Вывести сколько раз встречается каждое слово")
    print("3:Вывести отсортировать список слов")
    print("Введите любое другое число если хотите выйти")
    c = input("Введите что вы хотите сделать> ")
    if c == '1':
        avg_slov(s1)
    elif c == '2':
        create_dict(s1)
    elif c =='3':
        sort_dict(s1)
    else:
        break



