

















from tkinter import *
import time

root = Tk()

root.title("Fast Reading Assistant") # title
root.iconbitmap('C:/Users/Tamir/Python Projects/FastReading/book.ico') #icon 
screen_width = root.winfo_screenwidth() ### centering the window
screen_height = root.winfo_screenheight()

#window_width = 1024
#window_height = 768

window_width = int(screen_width)
window_height = int(screen_height)


# find the center point
#center_x = int(screen_width/2 - window_width / 2)
#center_y = int(screen_height/2 - window_height / 2)

center_x = -8
center_y = 0

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') ### centering the window

# head label
head_label = Label(root, text= "Fast Reading Assistant", font=("Tahoma", 18))
head_label.pack(pady=20)

# choose array size label
instructions_label = Label(root, text= "enter here the text you would like to read fast:", font=("Tahoma", 14))
instructions_label.pack(pady=10)


# array size textbox
reading_text_box = Text(root, width=55, height=8, font=("Tahoma", 12))
reading_text_box.pack(pady=20)

i = 0
def run():
    sentence = reading_text_box.get("1.0",'end-1c') # get the text
    sentence = sentence.split()
    
    def run_words():
        global i
        s = sentence[i]
        i = i + 1
        color = 'black'
        runnig_label.config(text=s, fg=color)
        if i < len(sentence):
            if speed_chosen.get() == "1 - Super Slow":
                speed = 500
            elif speed_chosen.get() == "2 - Slow":
                speed = 400
            elif speed_chosen.get() == "3 - Normal":
                speed = 300
            elif speed_chosen.get() == "4 - Quite-Fast":
                speed = 200
            elif speed_chosen.get() == "5 - Fast":
                speed = 100
            elif speed_chosen.get() == "6 - Super Fast":
                speed = 50

            root.after(speed, run_words) # speed delay
        else: # i == len(sentence)
            i = 0

    run_words()

speed_label = Label(root, text= 'select reading speed in the speed menu:', font=("Tahoma", 14))
speed_label.pack(pady=0)

# speed bar
#speed=StringVar()
#speed_entry = Entry(root,textvariable = speed, font=('calibre',20))
#speed_entry.pack(pady=10)

#creating option menu
options_list = ["1 - Super Slow" ,"2 - Slow", "3 - Normal", "4 - Quite-Fast", "5 - Fast", "6 - Super Fast"]
speed_chosen = StringVar(root)
speed_chosen.set("Select Reading Speed")
question_menu = OptionMenu(root, speed_chosen, *options_list)
question_menu.pack(pady=10)

    
start_reading_button = Button(root, width= 15, height= 3, font=("Tahoma 12 bold"), text="Start Reading", command= run)
start_reading_button.pack(pady=50)

runnig_label = Label(text='', font=("Tahoma 30")) # create runnig words label
runnig_label.pack(expand=True)

root.mainloop()
