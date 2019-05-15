from tkinter import  *#1
import random
#0) создаем окно
root=Tk()#2
root.title("Виселица")#3
canvas=Canvas(root, width=600, height=600)#6
canvas.pack()#7
#8) Рисуем фонв клеточку
def but():#9 Для этого сделаем отдельную функцию
    y=0#10 надо определиться по Х и по У, t. e. делать полоски, фон - белый, а линии - черный
    while y<600:#11 и мы будем рисовать У до 600
        x=0
        while x<600:#11 
            canvas.create_rectangle(x, y, x+33, y+27, fill="white", outline="blue")#12 Начинаем рисовать линии
            x=x+33#13 Теперь нужно смещать X и Y в правильном направлении
        y=y+27#14
#16but()#15  Теперь вызываем функцию стобы проверить
#17) здороваемся с игроком и объясняем правила, предлагаем начать
faq='''
Privet, davai poigraem.
Princip igri viselca:
Виселица — игра на бумаге для двух человек.
Один из игроков загадывает слово — пишет на бумаге первую 
и последнюю букву слова и отмечает места для остальных букв, 
например чертами (существует также вариант, когда изначально 
все буквы слова неизвестны). Также рисуется виселица с петлёй.
Согласно традиции русских лингвистических игр слово должно 
быть именем существительным нарицательным в именительном падеже 
единственного числа, либо множественного числа при отсутствии у 
слова формы единственного числа.
Второй игрок предлагает букву, которая может входить в это слово.
Если такая буква есть в слове, то первый игрок пишет её над 
соответствующими этой букве чертами — столько раз, сколько она 
встречается в слове. Если такой буквы нет, то к виселице 
добавляется круг в петле, изображающий голову. Второй игрок 
продолжает отгадывать буквы до тех пор, пока не отгадает всё
cлово. За каждый неправильный ответ первый игрок добавляет одну 
часть туловища к виселице (обычно их 6 - голова, туловище, 2 руки 
и 2 ноги, существует также вариант с 8 частями - добавляются 
ступни, а также самый длинный вариант, когда сначала за 
неотгаданную букву рисуются части самой виселицы).
Если туловище в виселице нарисовано полностью, то отгадывающий 
игрок проигрывает, считается повешенным. Если игроку удаётся 
угадать слово, он выигрывает и может загадывать слово.
'''#18
canvas.create_text(310, 240, text=faq, fill="purple",  font=("Helvetion", "14"))#19 Размести этот текст. Мы задаемкодрированное полложение текста
#23) создаем список слов
slova=["виселица", "смартфон", "маргарин", "мегагерц", "страница", "криветка", "микрофон"]#24
#25) В каждом слове выводим на экран только первую и последнюю букву. Остальое заменяем на _
def arr():#26 Создадим отдельную функцию
    but()#65
    word=random.choice(slova)#27 Мы должны выбрать случайное слово из нашего списка
    wo=word[1:-1]#29 Нжуно вернуть Все элементы списка, кроме 1-го и последнего
    wor=[]#28 занесем это все  отдельный список
    for i in wo:#30 заменим оставшиеся буквы на '_', то есть через этот цикл будем выводить новое слово
        wor.append(i)#31 добавляем в наш пустой список по одной букве
    a0=canvas.create_text(282, 40, text=word[0], fill="purple", font=("Helvetice","18"))#32
    a1= canvas.create_text(315, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a2= canvas.create_text(347, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a3= canvas.create_text(380, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a4= canvas.create_text(412, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a5= canvas.create_text(444, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a6= canvas.create_text(477, 40, text="_", fill="purple", font=("Helvetice", "18"))  # 32
    a6= canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Helvetice", "18"))  # 32
#35) Для неизвестных букв создаем список
    list1=[1,2,3,4,5,6]#36
    alfabet="абвгдеёжзийклмнопрстуфхцчшщъыьэюя" #37 Список всех возможных букв, которые мы будем применять и принимать ответ
    er=[]#38 создадим переменную, которая будет отвечать за ошибки
    win=[]#39
    def a(v): #40 создадим функцию, которая будет добавлять буквы и списки в указанные слова
        ind_alf = alfabet.index(v)#41 Теперь нужно выбрать буквы по индексу, которые у нас нажимаются
        key = alfabet[ind_alf]#42
        if v in wor:#43 Если буква, которую мы ввели в нашем слове и в пустом списке wor=[] записано, то мы должны вставить в список list[i zamenit], t.e, если V в списке wor
            ind=wor.index(v)#44 то мы должжны давать список list
            b2=list1[ind]#44
            wor[ind]='1'#45 и заменяем
            def kord():#60
                if b2==1:#61
                    x1,y1=315,40#62
                if b2==2:#61
                    x1,y1=347,40#62
                if b2==3:#61
                    x1,y1=380,40#62
                if b2==4:#61
                    x1,y1=412,40#62
                if b2==5:#61
                    x1,y1=444,40#62
                if b2==6:#61
                    x1,y1=477,40#62
                return x1, y1#63

            x1,y1 = kord()#64 задаем значение X и Y
            win.append(v)#57
            a2=canvas.create_text(x1, y1, text=wo[ind], fill="purple", font=("Helvetica", "18"))#58
            btn[key]["bg"]="green"#59 когда мы угадаем, нужно чтоб кнопки были зелеными
            if not v in wor:# 51 Теперь нужно разместить сами кнопки по Х и У
                btn[key]["stste"]="disabled"#52 эти кнопки будут находиться в выключенном состоянии
            if v in wor:
                win.append(v)#53 Тогда надо будет добавить в список
                ind2=wor.index(v)#54 Добавления индекса
                b2=list1[ind2]#55 добавить еще список
                x1, y1=kord()#75
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18"))#76
            if len(win)==6:#77 если длина равна 6
                canvas.create_text(150, 150, text="Ti pobedil", fill="purple", font=("Helvetica", "18"))#56 то напишем текст
                #69) проверяем правильность ответов
                for i in alfabet:#70 сделаем так, чтобы кнопки снова стали не нажатые
                    btn[i]["state"]="disabled"#71
        else:#72
            er.append(v)#73
            btn[key]["bg"]="red"#74
            btn[key]["state"]="disabled"#75 сделаем эту кнопку не активной
            if len(er)==1:#81 Если одна ошибка, то мы рисуем круг 
                golova()
            elif len(er)==2:#82
                telo()
            elif len(er)==3:#83
                rukaP()
            elif len(er)==4:#84
                rukaL()
            elif len(er)==5:  # 85
                nogaL()
            elif len(er)==6:  # 86
                nogaP()
                end()#87
            root.update()#91

    # 46) создаем кнопки с буквами
    btn={}
    def gen(u, x, y):#47 Теперь сделаем сами кнопки, для этого мы прописываем отдельную ффункцию и передаем значения по  X и Y

        #49btn[u]=Button(root, text=u, width=3, height=1)#47 сздать кнопку
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))  #50 Теперь когда мы нажали на кнопку, мы должны вызвать функцию a(v)
        btn[u].place(x=str(x), y=str(y))#48 и эту кнопку поставим
    x=265# 66 поставим теперь букву
    y=110
    for i in alfabet[0:8]:#67
        gen(i, x, y)#68 вызываем нашу функцию gen, размещаем кнопку в правильном положении по Х и У
        x=x+33#69 Смещаем каждую букву по Х на 33 px
    x=265
    y=137
    for i in alfabet[8:16]:
        gen(i, x, y)
        x=x+33
    x=265
    y=164
    for i in alfabet[16:24]:
        gen(i, x, y)
        x=x+33
    x=265
    y=191
    for i in alfabet[24:33]:
        gen(i, x, y)
        x=x+33#70 дожно вывести буквы из 4х строк

    # 9) рисуем части туловища
    def golova():#88
        canvas.create_oval(79, 59, 120, 80, width=4, fill='grey')#89
        root.update()#90
    def telo():
        canvas.create_line(100, 80, 100, 200, width=4)
        root.update()
    def rukaP():
        canvas.create_line(100, 80, 145, 100, width=4)
        root.update()
    def rukaL():
        canvas.create_line(100, 80, 45, 100, width=4)
        root.update()
    def nogaL():
        canvas.create_line(100, 200, 45, 300, width=4)
        root.update()
    def nogaP():
        canvas.create_line(100, 200, 145, 300, width=4)
        root.update()

    def end():#77
        canvas.create_text(150, 150, text="ti priogral",  fill="purple", font=("Helvetica", "18"))#78
        for i in alfabet:#79
            btn[i]["state"]="disabled"#80
#33 btn01=Button(root, text="Haachat", width=10, height=2)#20 Создаем кнопку для предложения игроку играть 
btn01 = Button(root, text="Haachat", width=10, height=1, command=lambda: arr())  #34 при нажатии на кнопку начать, мы вызываем эти слова

btn01.place(x=250, y=542)#21 расположим эту кнопку в Х и У по центру
btn01["bg"]="red"#22 сделаем кнопку красивой

root.mainloop()#4








