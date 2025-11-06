import tkinter as tk

window = tk.Tk()
print("Hello World")

window.title("My 2nd GUI Program")
window.minsize(500, 300)

#label
my_label = tk.Label(text="I am a label", font=("Arial", 25))
my_label.config(text="New Text")
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)

#button
def button_clicked():
    my_label.config(text="Button got clicked")
    print("I got clicked")

button = tk.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

def button_clicked_input():
    new_text = input.get()
    my_label.config(text=new_text)

input_button = tk.Button(text="New Button", command=button_clicked_input)
input_button.grid(column=2, row=0)


#entry
input = tk.Entry(width=10)
input.grid(column=4, row=3)






window.mainloop()
