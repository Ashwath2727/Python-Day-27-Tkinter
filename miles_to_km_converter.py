import tkinter as tk

window = tk.Tk()

def calculate_km():
    miles = int(miles_entry.get())
    kms = round(miles * 1.60934, 2)
    print(kms)
    km_answer.config(text=f"{kms}")

window.title("Miles to KM converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_entry = tk.Entry(width=10)
miles_entry.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_answer = tk.Label(text="0")
km_answer.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)




window.mainloop()