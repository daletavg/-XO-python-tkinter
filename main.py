from tkinter import *
from tkinter import messagebox
from random import randint

#ФУНКЦИЯ ЗАПУСКА ИГРЫ
def SetPlayerOrBot():
    player_to_player.config(state=DISABLED)
    player_to_bot.config(state=DISABLED)
    play_game.config(state=DISABLED)
    #РАЗБЛОКИРОВКА КНОПОК ЧТОБ МОЖНО БЫЛО ИГРАТЬ
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    button5.config(state=NORMAL)
    button6.config(state=NORMAL)
    button7.config(state=NORMAL)
    button8.config(state=NORMAL)
    button9.config(state=NORMAL)

ActivePlayer = 1
p1 = []
p2 = []
GamePoly = [1,2,3,4,5,6,7,8,9]


window = Tk()
window.title("Game")
window.geometry("300x400")
#############ВЫБОР ИГРЫ (ИГРОК С ИГРОКОМ | ИГРОК С БОТОМ)#################
player_or_bot=IntVar()
player_or_bot.set(0)
player_to_player = Radiobutton(window,text = "С игроком",value=0,variable=player_or_bot)
player_to_player.grid(row = 0, column = 0)

player_to_bot = Radiobutton(text = "С ботом",value=1,variable=player_or_bot)
player_to_bot.grid(row = 0, column = 1)

play_game = Button(window, text = "Играть",command=SetPlayerOrBot)
play_game.grid(row = 1, column = 2)
###########################################################################


#############КНОПКИ ДЛЯ ИГРЫ В КРЕСТИКИ НОЛИКИ############
button1 = Button(window, text = "",state=DISABLED)
button1.grid(row = 2, column = 0, ipadx = 40, ipady = 40)
button1.config(command = lambda: ButtonClick(1))

button2 = Button(window, text = "",state=DISABLED)
button2.grid(row = 2, column = 1, ipadx = 40, ipady = 40)
button2.config(command = lambda: ButtonClick(2))

button3 = Button(window, text = "",state=DISABLED)
button3.grid(row = 2, column = 2, ipadx = 40, ipady = 40)
button3.config(command = lambda: ButtonClick(3))

button4 = Button(window, text = "",state=DISABLED)
button4.grid(row = 3, column = 0, ipadx = 40, ipady = 40)
button4.config(command = lambda: ButtonClick(4))

button5 = Button(window, text = "",state=DISABLED)
button5.grid(row = 3, column = 1, ipadx = 40, ipady = 40)
button5.config(command = lambda: ButtonClick(5))

button6 = Button(window, text = "",state=DISABLED)
button6.grid(row = 3, column = 2, ipadx = 40, ipady = 40)
button6.config(command = lambda: ButtonClick(6))

button7 = Button(window, text = "")
button7.grid(row = 4, column = 0, ipadx = 40, ipady = 40)
button7.config(command = lambda: ButtonClick(7))

button8 = Button(window, text = "",state=DISABLED)
button8.grid(row = 4, column = 1, ipadx = 40, ipady = 40)
button8.config(command = lambda: ButtonClick(8))

button9 = Button(window, text = "",state=DISABLED)
button9.grid(row = 4, column = 2, ipadx = 40, ipady = 40)
button9.config(command = lambda: ButtonClick(9))
##########################################################


#ФУНКЦИЯ УСТАНОВКИ КРЕСТИКА ИЛИ НОЛИКА
def ButtonClick(id):
  global ActivePlayer
  global GamePoly
  global p1
  global p2
  print("ID:{}".format(id))
  if (ActivePlayer == 1):
    SetLayout(id, "X")
    p1.append(id)
    GamePoly.remove(id)

    if player_or_bot.get() ==1:
        # ЕСЛИ ВЫБГРАЛИ БОТА, ТОГДА БУДЕТ ХОДИТЬ БОТ
        num_bot = AutoPlay()
        if num_bot ==0:
            ChooseWinner()
        SetLayout(num_bot, "O")
        p2.append(num_bot)
        GamePoly.remove(num_bot)
        ActivePlayer = 1
    else:
        ActivePlayer = 2
    print("P1:{}".format(p1))
  elif (ActivePlayer == 2):
    SetLayout(id, "O")
    p2.append(id)
    ActivePlayer = 1
    print("P2:{}".format(p2))


  ChooseWinner()
#УСТАНОВКА КРЕСТИКА ИЛИ НОЛИКА НА КНОПКУ
def SetLayout(id, PlayerSymbol):
  if (id == 1):
    button1.config(text = PlayerSymbol, state = DISABLED)
  elif (id == 2):
    button2.config(text = PlayerSymbol, state = DISABLED)
  elif (id == 3):
    button3.config(text = PlayerSymbol, state = DISABLED)
  elif (id == 4):
    button4.config(text = PlayerSymbol, state = DISABLED)
  elif (id == 5):
    button5.config(text = PlayerSymbol, state = DISABLED)
  elif (id == 6):
    button6.config(text = PlayerSymbol, state = DISABLED)
  elif (id == 7):
    button7.config(text = PlayerSymbol, state = DISABLED)
  elif (id == 8):
    button8.config(text = PlayerSymbol, state = DISABLED)
  elif (id == 9):
    button9.config(text = PlayerSymbol, state = DISABLED)
#ПРОВЕРКА ВЫЙГРАША
def ChooseWinner():
  Winner = 0
  ''' W I N N E R - 1 '''
  if ((1 in p1) and (2 in p1) and (3 in p1)):
    Winner = 1
  if ((1 in p2) and (2 in p2) and (3 in p2)):
    Winner = 2
  if ((4 in p1) and (5 in p1) and (6 in p1)):
    Winner = 1
  if ((4 in p2) and (5 in p2) and (6 in p2)):
    Winner = 2
  if ((7 in p1) and (8 in p1) and (9 in p1)):
    Winner = 1
  if ((7 in p2) and (8 in p2) and (9 in p2)):
    Winner = 2
  ''' W I N N E R - 2 '''
  if ((1 in p1) and (4 in p1) and (7 in p1)):
    Winner = 1
  if ((1 in p2) and (4 in p2) and (7 in p2)):
    Winner = 2
  if ((2 in p1) and (5 in p1) and (8 in p1)):
    Winner = 1
  if ((2 in p2) and (5 in p2) and (8 in p2)):
    Winner = 2
  if ((3 in p1) and (6 in p1) and (9 in p1)):
    Winner = 1
  if ((3 in p2) and (6 in p2) and (9 in p2)):
    Winner = 2
  ''' W I N N E R - 3 '''
  if ((1 in p1) and (5 in p1) and (9 in p1)):
    Winner = 1
  if ((1 in p2) and (5 in p2) and (9 in p2)):
    Winner = 2
  if ((3 in p1) and (5 in p1) and (7 in p1)):
    Winner = 1
  if ((3 in p2) and (5 in p2) and (7 in p2)):
    Winner = 2
  if Winner == 1:
    messagebox.showinfo("Winner", "Player 1 is Winner")
  elif Winner == 2:
    messagebox.showinfo("Winner", "Player 2 is Winner")
  elif Winner == 2 and player_or_bot.get()==1:
      #СРАБОТАЕТ ЕСЛИ ВЫБРАН БОТ
      messagebox.showinfo("Winner", "BOT is Winner")


#ФУНКЦИЯ ДЛЯ ТОГО ЧТОБ ХОДИЛ БОТ
def AutoPlay():
  global p1
  global p2
  global GamePoly
  RandomIndex = 0
  while True:
    RandomIndex = randint(1, 9)
    for i in range(9):
        if len(GamePoly)==0:
            return 0
        elif ((RandomIndex in p1) or (RandomIndex in p2)):
            continue
        else:
            return RandomIndex

window.mainloop()
