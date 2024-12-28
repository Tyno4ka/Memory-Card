from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
QLabel, 
QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton,
QPushButton,QButtonGroup)
from random import shuffle,randint

class Qeuestion():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Qeuestion('Язык бразилии ?','португальский','руский','английский','румынский'))
question_list.append(Qeuestion('Какого цвета нет в флаге России?',"желтый","синий",'красный','белый'))
question_list.append(Qeuestion("Какой национальности не существует?",'Энцы','Смурфы','Чулымцы','Алеуты'))
question_list.append(Qeuestion("Какого бойца ент в бравл старс?",'гения','гейла','ворона','вольта'))
question_list.append(Qeuestion("Какой буквы не было в названии тоботов?",'k','X','Y','Z'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('')
main_layout = QVBoxLayout()

RadioGroupBox = QGroupBox("варианты ответа")
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton("Алеуты")
layout_an1 = QHBoxLayout()
layout_an2 = QVBoxLayout()
layout_an3 = QVBoxLayout()

layout_an2.addWidget(rbtn_1)
layout_an2.addWidget(rbtn_2)
layout_an3.addWidget(rbtn_3)
layout_an3.addWidget(rbtn_4)
layout_an1.addLayout(layout_an2)
layout_an1.addLayout(layout_an3)

RadioGroupBox.setLayout(layout_an1)

AnsGroupBox = QGroupBox()
Results = QLabel('правильно/неправильно')
Correct = QLabel("ответ тут")
window.score = 0
window.total = 0

layout_ret = QVBoxLayout()
layout_ret.addWidget(Results,alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_ret.addWidget(Correct, alignment = Qt.AlignHCenter , stretch=2)
AnsGroupBox.setLayout(layout_ret)

vopros = QLabel('Какой национальности не существует?')
ans = QPushButton("Ответить")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(vopros,alignment = (Qt.AlignVCenter|Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(ans,stretch =2)
layout_line3.addStretch(1)

main_layout.addLayout(layout_line1)
main_layout.addLayout(layout_line2)
main_layout.addLayout(layout_line3)
main_layout.setSpacing(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    ans.setText('Следуюший вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    ans.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1 , rbtn_2 , rbtn_3 , rbtn_4]
def ask (q = Qeuestion):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    vopros.setText(q.question)
    Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    Results.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("правильно")
        window.score += 1
    else:
        if  answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("неверно")

def next_question():
    window.total += 1
    if window.total != 0 :
        print("статистика:",window.total,window.score, "\n объщий результат:",window.score/window.total*100)
    cur_question = randint(0 , len(question_list) -1)
    q = question_list[cur_question]
    ask(q)



def click_ok():
    if "Ответить" == ans.text():
        check_answer()
    else:
        next_question()


window.setLayout(main_layout)


#создай приложение для запоминания информации
window.total = -1
window.score = 0
ans.clicked.connect(click_ok)
next_question()
window.show()
app.exec()