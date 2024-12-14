import random
import tkinter as tk
from PIL import Image, ImageTk
from options import *
from Player import *
import pygame
from Animation import *


class TextAdventureGame:
    gamer = Player()
    def __init__(self, master):

        gamer = Player()
        self.master = master
        master.title("Текстовый квест")

        # Музыка
        pygame.mixer.init()
        pygame.mixer.music.load("Hylics 2 - Xeno Arcadia.mp3")
        pygame.mixer.music.play(-1)


        # Загрузка изображения фона
        self.background_image = ImageTk.PhotoImage(Image.open("background.png").resize((960, 720)))
        self.background_label = tk.Label(master, image=self.background_image)
        self.background_label.place(x=0, y=0)

        # Портрет игрока
        self.player_image = ImageTk.PhotoImage(Image.open("player_portrait.png").resize((200, 200)))  # Убедитесь, что размер изображения подходит
        self.player_label = tk.Label(master, image=self.player_image)
        self.player_label.place(x=60, y=20)



        # Имя игрока
        self.name_box = tk.Text(master, wrap='word', height = 2, width=25, bg = "#c7bfad", fg="#781F19")
        self.name_box.place(relx=0.165, rely = 0.35, anchor = 'center')
        self.name_box.insert(tk.END, gamer.name)
        self.name_box.config(state = 'disabled')

        # Характеристики игрока
        self.char_box1 = tk.Text(master, wrap='word', height=1, width=2, bg = "#c7bfad", fg="#781F19")
        self.char_box1.place(relx=0.155, rely=0.4, anchor='center')
        self.char_box1.insert(tk.END, gamer.strength)
        self.char_box1.config(state='disabled')

        self.char_name_box1 = tk.Text(master, wrap='word', height=1, width=5, bg = "#c7bfad", fg="#781F19")
        self.char_name_box1.place(relx=0.1, rely=0.4, anchor='center')
        self.char_name_box1.insert(tk.END, "Сила:")
        self.char_name_box1.config(state='disabled')

        self.char_box2 = tk.Text(master, wrap='word', height=1, width=2, bg = "#c7bfad", fg="#781F19")
        self.char_box2.place(relx=0.155, rely=0.45, anchor='center')
        self.char_box2.insert(tk.END, gamer.intelligent)
        self.char_box2.config(state='disabled')

        self.char_name_box2 = tk.Text(master, wrap='word', height=1, width=10, bg = "#c7bfad", fg="#781F19")
        self.char_name_box2.place(relx=0.1, rely=0.45, anchor='center')
        self.char_name_box2.insert(tk.END, "Интеллект:")
        self.char_name_box2.config(state='disabled')

        self.char_box3 = tk.Text(master, wrap='word', height=1, width=2, bg = "#c7bfad", fg="#781F19")
        self.char_box3.place(relx=0.155, rely=0.5, anchor='center')
        self.char_box3.insert(tk.END, gamer.charisma)
        self.char_box3.config(state='disabled')

        self.char_name_box1 = tk.Text(master, wrap='word', height=1, width=9,bg = "#c7bfad", fg="#781F19")
        self.char_name_box1.place(relx=0.1, rely=0.5, anchor='center')
        self.char_name_box1.insert(tk.END, "Харизма:")
        self.char_name_box1.config(state='disabled')

        # Текстовая область
        self.text_box = tk.Text(master, wrap='word', height=15, width=40, bg = "#c7bfad", fg="#781F19", font = "Courier 15")
        self.text_box.place(relx=0.665, rely=0.4, anchor='center')
        self.text_box.insert(tk.END, "Вас отправили на важное задание. Что вы хотите сделать?")
        self.text_box.config(state='disabled')  # Запрет редактирования

        # картинка замка (появляется только в начале, а после исчезает)
        self.castle_image = ImageTk.PhotoImage(
            Image.open("castle.png").resize((435, 210)))
        self.castle_label = tk.Label(master, image=self.castle_image)
        self.castle_label.pack()
        #self.castle_label.place(x=420, y=240)
        self.castle_label.pack_forget()

        #FIREBAAAAAAALL
        self.FIREBALL_image = ImageTk.PhotoImage(
            Image.open("fireball.webp").resize((435, 244)))
        self.simple_fireball_image = ImageTk.PhotoImage(Image.open("old_fireball.jpg").resize((435,244)))
        self.FIREBALL_label = tk.Label(master, image=self.FIREBALL_image)
        self.FIREBALL_label.pack()
        # self.castle_label.place(x=420, y=240)
        self.FIREBALL_label.pack_forget()

        # Кнопка настройки звука
        self.button1 = tk.Button(master, text="Настройка звука", command=self.settings, bg = "#c7bfad", fg="#781F19")
        self.button1.place(relx=0.2, rely=0.8, anchor='center')

        # Кнопки
        self.button1 = tk.Button(master, text="Идти вперёд", command=self.start, bg = "#c7bfad", fg="#781F19")
        self.button1.pack()
        self.button1.place(relx=0.45, rely=0.8, anchor='center')

        self.button2 = tk.Button(master, text=" ", command=self.option1_3, bg = "#c7bfad", fg="#781F19")
        self.button2.pack()
        #self.button2.place(relx=0.656, rely=0.8, anchor='center')
        self.button2.pack_forget()

        self.button3 = tk.Button(master, text=" ", bg = "#c7bfad", fg="#464646")
        self.button3.pack()
        #self.button3.place(relx=0.9, rely=0.8, anchor='center')
        self.button3.pack_forget()

        self.button_end = tk.Button(master, text="Закончить игру", command = self.close, bg = "#c7bfad", fg="#781F19")
        self.button_end.place(relx = 0.2, rely = 0.6, anchor = 'center')

        self.button_restart = tk.Button(master, text="Начать заново", command = self.restart, bg = "#c7bfad", fg="#781F19")
        self.button_restart.place(relx=0.2, rely=0.7, anchor='center')

        self.button_restart = tk.Button(master, text="Перегенерировать характеристики", command=self.re_char, bg = "#c7bfad", fg="#781F19")
        self.button_restart.place(relx=0.2, rely=0.9, anchor='center')

    def settings(self):
        root = tk.Tk()
        root.title("Настройка звука")
        root.geometry("200x100")
        # Слайдер для регулировки громкости
        volume_slider = tk.Scale(root, from_=0, to=100, orient='horizontal', label='', command=self.set_volume)
        # volume_slider.config(relx = 0.2, rely = 0.85)
        volume_slider.set(100)  # Установка начального значения громкости на 100%
        # volume_slider.place(relx = 0.2, rely = 0.85, relwidth=10 )
        volume_slider.pack()

    def show_button(self, num):
        if num == 1 :
            self.button1.pack()
            self.button1.place(relx=0.45, rely=0.8, anchor='center')
        elif num == 2:
            self.button2.pack()
            self.button2.place(relx=0.656, rely=0.8, anchor='center')
        elif num == 3:
            self.button3.pack()
            self.button3.place(relx=0.9, rely=0.8, anchor='center')

    def set_volume(self, value):
        volume = float(value) / 100  # Преобразование в диапазон от 0.0 до 1.0
        pygame.mixer.music.set_volume(volume)

    def re_char(self):
        #self.gamer.reset_char()
        self.gamer.charisma = random.randint(5, 15)
        self.gamer.intelligent = random.randint(5, 15)
        self.gamer.strength = random.randint(5, 15)

        self.char_box1.config(state='normal')
        self.char_box1.delete('1.0', tk.END)
        self.char_box1.insert(tk.END, self.gamer.strength)
        self.char_box1.config(state='disabled')
        self.char_box2.config(state='normal')
        self.char_box2.delete('1.0', tk.END)
        self.char_box2.insert(tk.END, self.gamer.intelligent)
        self.char_box2.config(state='disabled')
        self.char_box3.config(state='normal')
        self.char_box3.delete('1.0', tk.END)
        self.char_box3.insert(tk.END, self.gamer.charisma)
        self.char_box3.config(state='disabled')
        #self.char_box2.insert(tk.END, self.gamer.intelligent)
        #self.char_box1.insert(tk.END, self.gamer.strength)
        #self.char_box3.insert(tk.END, self.gamer.charisma)

    def update_text(self, new_text):
        self.text_box.config(state='normal')
        self.text_box.delete('1.0', tk.END)
        self.text_box.insert(tk.END, new_text)
        self.text_box.config(state='disabled')

    def restart_buttons(self):
        self.button3.config(text="")
        self.button2.config(text="")
        self.button1.config(text="")
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button1.pack_forget()
        self.button2.pack_forget()
        self.button3.pack_forget()

    def start(self):
        # rand = random.randint(1,2)
        rand = 1
        if rand==1 : self.option1_1()
        # else : self.option2_1()
        # print("start")

    def close(self):
        pygame.mixer.music.stop()
        self.master.destroy()

    def restart(self):
        self.restart_buttons()
        self.button1.config(text = "Идти вперёд", command=self.start)
        self.show_button(1)
        self.update_text("Вас отправили на важное задание. Что вы хотите сделать?")


     # развития сюжета

    def option1_1(self):
        self.castle_label.pack()
        self.castle_label.place(x=420, y=240)
        self.update_text("Вы идете налево и находите старый замок.")
        self.button1.config(text= "Войти в замок", command= self.option1_2)
        self.button2.config(text="Осмотреть замок", command=self.option1_3)
        self.show_button(2)
        self.show_button(3)
        self.button3.config(text="Пустить в замок\n огненный шар", command = lambda : self.option_pre_end(end4))


    def option1_2(self) :
        self.update_text("В замке что-то происходит.")
        self.button3.pack()
        self.button3.pack_forget()
        self.show_button(1)
        self.show_button(2)
        self.button1.config(text= op1, command = self.option1_4 )
        self.button2.config(text=op2, command = self.option1_5)

    def option1_3(self):
        self.update_text("Обычный замок. Не то чтобы вы видели много замков, но этот кажется максимально обычным.")
        self.button3.pack()
        self.button3.pack_forget()
        self.button1.config(text="Задаться вопросами\n об архитектуре \n и смысле существования\n замков",
                            command= lambda : self.option_pre_end(end7))
        self.button2.config(text="Всё-таки пустить фаербол",
                            command= lambda : self.option_pre_end(end4))

    def option1_4(self):
        if self.gamer.intelligent >= 10 :
            self.castle_label.pack()
            self.castle_label.pack_forget()
            self.FIREBALL_label.pack()
            self.FIREBALL_label.place(x=420, y=255)
            self.update_text(rep1)
            self.show_button(1)
            self.show_button(2)
            self.show_button(3)
            self.button3.config(text = "Несомненно", command=lambda : self.option_pre_end(end4))
            self.button2.config(text = "Да", command=lambda : self.option_pre_end(end4))
            self.button1.config(text = "Конечно", command=lambda : self.option_pre_end(end4))
        else:
            self.update_text(rep2)
            self.restart_buttons()
            self.show_button(2)
            self.button2.config(text = op2, command=self.option1_5)


    def option1_5(self):
        self.castle_label.pack()
        self.castle_label.pack_forget()
        if self.gamer.charisma >=10 :
            self.option_pre_end(rep3)
        else:
            self.update_text(rep4)
            self.restart_buttons()
            self.show_button(2)
            self.button2.config(text = "В бой!", command=self.start_battle)


    def option_pre_end(self, end):
        self.castle_label.pack()
        self.castle_label.pack_forget()
        self.FIREBALL_label.pack()
        self.FIREBALL_label.pack_forget()
        self.update_text(end)
        self.button2.config( text="")
        self.button2.pack()
        self.button2.pack_forget()
        self.show_button(1)
        self.button1.config(text="Моя работа здесь окончена",
                          command=self.fin)
        self.button3.pack()
        self.button3.pack_forget()
        self.button3.config(text="")


    def start_battle(self):
        pygame.mixer.music.stop()
        battle = Animation()
        pygame.mixer.init()
        pygame.mixer.music.load("Hylics 2 - Xeno Arcadia.mp3")
        pygame.mixer.music.play(-1)
        self.option_pre_end(test_op)
        #pygame.mixer.music.play(-1)

    def fin(self):
        self.castle_label.pack()
        self.castle_label.pack_forget()
        self.update_text("Конец.")
        self.restart_buttons()
        self.show_button(1)
        self.show_button(2)
        self.button1.config(text = "Начать заново", command=self.restart)
        self.button2.config(text = "Выйти", command= self.close)
