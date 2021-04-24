#создай приложение для запоминания информации

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint



class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('гусей было 5, сколько стало гусей если 2 из них пошли на суп?','3','1','4','5'))
questions_list.append(Question('У гусей было 3 брата, 1 из них пошёл на гриль, а 1 пошёл в духовку, сколькоиз этих братьев выжило?','1','0','2','5'))
questions_list.append(Question('Охотник решил убить чаосового , но он промахнулся и на него напало 50% часовых от 2 и забили его досмерти, сколько часовых забило досмерти охотника?','1','3','4','5'))
questions_list.append(Question('На суп пошло 2 часовых, 1 сыч, 1 гусь, сколько всего ингредиентов пошло на суп?','4','2','3','5'))
questions_list.append(Question('4 человека пошло на охоту на часовых.Половину из них забили часовые, сколько охотников погибло при схватке с часовыми?','2','1','3','5'))
questions_list.append(Question('Однажды охотники решили сварить сычей на гриле.Они их замариновали пармизаном лучком и тд, и вот когда надо было уже класть их нагриль один охотник опрокинул тарелку с сычами а их там было 3 , а всего сычей было 5, сколько сычей пошло на гриль?','2','1','3','5'))
questions_list.append(Question('30 гусей захотели поесть сычей и часовых, но когда они начали на них охоту в 1 гуся ударила молния и он умер,сколько гусей осталось в живых?','29','6','1','30'))
questions_list.append(Question('Часовой любил есть малинку, но однажды малинка  кончилась и он здох от голода, сколько минут часовой прожил без малинки если минут было 50% от 2?','1','0','2','3'))
questions_list.append(Question('Гусь хотел умереть не обычным способом и он позвал часового для драки, но часовой оказался хитёр и умер ещё до того как к нему пришёл гусь и тогда гусь решил жить дальше, сколько лет дальше жил гусь если он жил 5 + 6 ЛЕТ?','11','5','6','0'))
questions_list.append(Question('Рецепт утки по пекински состоит из: лучка, чачи, чесночка, утки, соли, перца, помидора, масла, и смерти.Сколько компанентов пошло на утку по пекински?','9','1','4','5'))

app = QApplication([])
 
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
# ----------------------------------------------------------
# Виджеты и макеты созданы, далее - функции:
# ----------------------------------------------------------
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1,rbtn_2, rbtn_3, rbtn_4]
#def test():
 #   ''' временная функция, которая позволяет нажатием на кнопку вызывать по очереди
   # show_result() либо show_question() '''
   # if 'Ответить' == btn_OK.text():
   #     show_result()
    #else:
 #       show_question()

def ask (q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()



def show_correct(res):
    lb_Result.setText(res)
    show_result()

f = []
f.append(ask)


g_gg = 0


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.correct = window.correct + 1
        print("Статистика: правильных ответов ", window.correct, 'Весго вопросов ', window.total )
        print("Рейтинг: ", (window.correct/window.total * 100), "%")
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно!')
        print("Статистика: правильных ответов ", window.correct, 'Весго вопросов ', window.total )
        print("Рейтинг: ", (window.correct/window.total * 100), "%")
    print(window.correct)
        

def next_question():
    window.total = window.total + 1
    print("Статистика: правильных ответов ", window.correct, 'Весго вопросов ', window.total )
    print("Рейтинг: ", window.correct/window.total * 100, "%")
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    print(window.total)
    ask(q)
    

def click_ok():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()


    
 
window = QWidget()
window.correct = 0
window.total = 0
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.cur_question = -1
next_question()
btn_OK.clicked.connect(click_ok)
window.show()
app.exec_()