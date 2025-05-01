from tkinter import *

def button_clicked():
    a = float(miles_input.get()) * 1.609
    equal_result.config(text=round(a, 1))

window = Tk()
window.title('My first GUI program')
window.minsize(width=250, height=150)
window.config(pady=20, padx=20)



#Label
equal = Label(text="is equal to", font=("Arial", 14))
equal.grid(column=0, row=1)

equal_result = Label(width=10)
equal_result.grid(column=1, row=1)

miles = Label(text='Miles')
miles.grid(column=2, row=0)

km = Label(text='Km')
km.grid(column=2, row=1)



#Button
calculate = Button(text='Click Me', command=button_clicked)
calculate.grid(column=1, row=2)



#Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


window.mainloop()