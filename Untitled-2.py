from tkinter import *
def on_calculate():
    if calc_entry.index("end") == 0:
        result_label.config(text="Введите выражение!")
        return
    expression = calc_entry.get()
    try:
        result = eval(expression)
    except Exception as ex:
        result_label.config(text=ex)
        return
    result_label.config(text=result)
root = Tk()
root.title("Калькулятор")
frame_1 = Frame()
frame_2 = Frame()
calc_entry = Entry(frame_1)
calculate_button = Button(frame_1, text='Вычислить', command=on_calculate)
result_label = Label(frame_2)
frame_1.pack()
frame_2.pack()
calc_entry.pack(side=LEFT)
calculate_button.pack(side=RIGHT)
result_label.pack(side=BOTTOM)
root.mainloop()