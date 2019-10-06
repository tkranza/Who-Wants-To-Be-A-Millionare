from tkinter import *
import tkinter.messagebox
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from question import *

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text='play music', command=self.play_sound,bg="blue", fg="white")
        self.button.pack(side=RIGHT)
        self.button2 = Button(frame, text='stop music', command=self.stop_sound,bg="blue", fg="white")
        self.button2.pack(side=RIGHT)
        PlaySound('sound.wav', SND_FILENAME | SND_LOOP | SND_ASYNC)

    def play_sound(self):
        PlaySound('sound.wav', SND_FILENAME|SND_LOOP|SND_ASYNC)

    def stop_sound(self):
        PlaySound(None, SND_FILENAME)

root = Tk()
root.title("Who Wants To Be A Millionare?")
root.configure(background='midnight blue')
app = App(root)

def TocanOdg(quest, nm):
    global number
    global button1
    global button2
    global button3
    global button4
    global button5
    answer = tkinter.messagebox.askquestion('', "Is this your final answer?")
    if answer == 'yes':
        if(quest.wrong_answers[nm] == quest.answer):
            tkinter.messagebox.showinfo("", "Congratulations, correct answer!")
        else:
            tkinter.messagebox.showinfo("", "Wrong answer, Game Over!")
            root.quit()
    if answer == 'no':
        return
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    number = number + 1
    if(number < 15):
        button1 = Button(frame2, text="A: " + pitanja[number].wrong_answers[0], command=lambda: TocanOdg(pitanja[number], 0), bg="blue", fg="white",padx = 40)
        button1.grid(row=1)
        button2 = Button(frame2, text="B: " + pitanja[number].wrong_answers[1], command=lambda: TocanOdg(pitanja[number], 1), bg="blue", fg="white",padx = 40)
        button2.grid(row=1, column=2)
        button3 = Button(frame2, text="C: " + pitanja[number].wrong_answers[2], command=lambda: TocanOdg(pitanja[number], 2), bg="blue", fg="white",padx = 40)
        button3.grid(row=2)
        button4 = Button(frame2, text="D: " + pitanja[number].wrong_answers[3], command=lambda: TocanOdg(pitanja[number], 3), bg="blue", fg="white",padx = 40)
        button4.grid(row=2, column=2)
        button5 = Button(frame2, text=pitanja[number].prompt, bg="blue", fg="white",padx = 80)
        button5.grid(columnspan=3, row=0)
    else:
        tkinter.messagebox.showinfo("", "Congratulations, You Won Million Dollars!")
        root.quit()


root.geometry("1366x768")

frame1 = Frame(root, width = 500, height = 500)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame2.configure(background='midnight blue')

photo1 = PhotoImage(file="background.png")
label1 = Label(frame1, image = photo1)
label1.pack()

number = 0

button1 = Button(frame2, text="A: " + pitanja[number].wrong_answers[0], command=lambda: TocanOdg(pitanja[number], 0), bg="blue", fg="white",padx = 40)
button1.grid(row=1)
button2 = Button(frame2, text="B: " + pitanja[number].wrong_answers[1], command=lambda: TocanOdg(pitanja[number], 1), bg="blue", fg="white",padx = 40)
button2.grid(row=1, column=2)
button3 = Button(frame2, text="C: " + pitanja[number].wrong_answers[2], command=lambda: TocanOdg(pitanja[number], 2), bg="blue", fg="white",padx = 40)
button3.grid(row=2)
button4 = Button(frame2, text="D: " + pitanja[number].wrong_answers[3], command=lambda: TocanOdg(pitanja[number], 3), bg="blue", fg="white",padx = 40)
button4.grid(row=2, column=2)
button5 = Button(frame2, text=pitanja[number].prompt, bg="blue", fg="white",padx = 80)
button5.grid(columnspan=3, row=0)

root.mainloop()