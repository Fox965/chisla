import random

flag = True
while flag:
    def cel():
        i = 5
        while i <= 100:
            i += 5
            random.seed()
            print([random.randint(0, 10000) for i in range (5)])
    def drob():
        i = 5
        while i <= 100:
            i += 5
            random.seed()
            print(['%.2f' % random.uniform(0, 10000) for i in range (5)])
    num = int(input("Нажмите 1 - для вывода ГПСЧ с целыми числами \n"
                        "Нажмите 2 - для вывода ГПСЧ с вещественными числами "))
    if num == 1:
        cel()
    if num == 2:
        drob()

    flag = True if input('Начать заново?(y/n) ') == 'y' else False
