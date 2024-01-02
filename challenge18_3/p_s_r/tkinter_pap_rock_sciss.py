import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk
import os
print(os.getcwd())

window = tk.Tk()

window.title("Paper-Rock-Scissors")
window.geometry("800x600")

window.columnconfigure([0, 1, 2], weight=1)
window.rowconfigure([0, 1], weight=1)

frame1 = tk.Frame(window, relief=tk.RAISED, borderwidth=5)
frame1.grid(row=0, column=1)
frame1.columnconfigure([0, 1, 2], weight=1)
frame1.rowconfigure(0, weight=1)
title_lbl = tk.Label(frame1, text="Let's play!\n\nPress one of the buttons to make a choice!", font="Arial")
title_lbl.grid(row=0, column=1, sticky='n', pady=(0, 15))
 
img1_path = "ZaRaczke\\challenge18_3\\p_s_r\\images\\paper.png"
img2_path = 'ZaRaczke\\challenge18_3\\p_s_r\\images\\rock.png'
img3_path = 'ZaRaczke\\challenge18_3\\p_s_r\\images\\scissors.png'

     
#tworzenie obiektów obrazow przyciskow
img1 = tk.PhotoImage(file=img1_path)
img2 = tk.PhotoImage(file=img2_path)
img3 = tk.PhotoImage(file=img3_path)
#lista do losowania "wyboru" komputera
img_list = [img1, img2, img3]

def computer_choose():
    #wybor komputera
    chosen_by_compter = random.choice(img_list)
    lbl_comp_chosen['image'] = chosen_by_compter
    return chosen_by_compter

def button_clicked(btn):
    computer_choose()
    player_choice = btn['image']
    computer_choice = lbl_comp_chosen["image"]
    
    if player_choice == computer_choice:
        lbl_winner_text['text'] = "Draw!"
    elif (player_choice == str(img1)) and (computer_choice == str(img2)) or \
         (player_choice == str(img2)) and (computer_choice == str(img3)) or \
         (player_choice == str(img3)) and (computer_choice == str(img1)):
        lbl_winner_text['text'] = "Player wins"
    else:
        lbl_winner_text['text'] = "Machine wins!"
    
    
button_paper = tk.Button(frame1, image=img1, height=150, width=150, command=lambda:button_clicked(button_paper))
button_paper.grid(row=1, column=0, padx=(20, 0), sticky='e')    

button_rock = tk.Button(frame1, image=img2, height=150, width=150, command=lambda:button_clicked(button_rock))
button_rock.grid(row=1, column=1, )

button_scissors = tk.Button(frame1, image=img3, height=150, width=150, command=lambda:button_clicked(button_scissors))
button_scissors.grid(row=1, column=2, padx=(0,20), sticky='w')



lbl_comp_text=tk.Label(frame1, text="The computer has chosen:", font="Arial")
lbl_comp_text.grid(row=2, column=1, pady=40)

lbl_comp_chosen = tk.Label(frame1, image='')
lbl_comp_chosen.grid(row=3, rowspan=3, column=1)

lbl_winner_text=tk.Label(frame1, text="", font="Arial")
lbl_winner_text.grid(row=7, column=1, sticky='s')





window.mainloop()        

