import tkinter as tk

window = tk.Tk()

window.title("My First GUI Program")
window.minsize(500, 300)

#label
my_label = tk.Label(text="I am a label", font=("Arial", 25))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#button
def button_clicked():
    my_label.config(text="Button got clicked")
    print("I got clicked")

button = tk.Button(text="Click me", command=button_clicked)
button.pack()

#entry
input = tk.Entry(width=10)
input.pack()

def button_clicked_input():
    new_text = input.get()
    my_label.config(text=new_text)

input_button = tk.Button(text="Click ok", command=button_clicked_input)
input_button.pack()

#text
text = tk.Text(width=30, height=5)
text.focus()
text.insert(tk.END, "example of multiline text entry")
print(text.get("1.0", tk.END))
text.pack()

#spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale
def scale_used(value):
    print(value)

scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = tk.IntVar()
checkedbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkedbutton.pack()

#radiobutton
def radio_used():
    print(radio_state.get())
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton1.pack()

radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton2.pack()


#listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()




window.mainloop()