import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(500, 300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 25))
my_label.pack()


window.mainloop()