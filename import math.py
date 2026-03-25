import math
from tkinter import *

# Функции для математических операций
def evaluate_expression(expression):
    try:
        # Безопасный eval с обработкой математических функций
        result = eval(expression, {"__builtins__": None, "math": math})
        return result
    except Exception as ex:
        return f"Ошибка: {ex}"

def on_calculate():
    expression = calc_entry.get()
    if not expression:
        result_label.config(text="Введите выражение!")
        return
    result = evaluate_expression(expression)
    result_label.config(text=result)

def clear_input():
    calc_entry.delete(0, END)
    result_label.config(text="")

def add_function_buttons():
    # Создает кнопки для математических функций
    functions = [
        ("sin", "math.sin({})"),
        ("cos", "math.cos({})"),
        ("tan", "math.tan({})"),
        ("√", "math.sqrt({})"),
        ("log", "math.log10({})")
    ]
    for (text, formula) in functions:
        btn = Button(func_frame, text=text, command=lambda f=formula: insert_function(f))
        btn.pack(side=LEFT)

def insert_function(formula):
    # Вставляет функцию в поле ввода
    current_text = calc_entry.get()
    calc_entry.delete(0, END)
    calc_entry.insert(END, formula.format(current_text))

# Создаем главное окно
root = Tk()
root.title("Расширенный калькулятор")

# Создаем рамки для ввода и результата
frame_input = Frame(root)
frame_buttons = Frame(root)
frame_result = Frame(root)

# Поле ввода
calc_entry = Entry(frame_input, width=30)
# Кнопка вычисления
calculate_button = Button(frame_input, text="Вычислить", command=on_calculate)
# Кнопка очистки
clear_button = Button(frame_input, text="Очистить", command=clear_input)

# Размещение элементов
calc_entry.pack(side=LEFT, padx=5)
calculate_button.pack(side=LEFT, padx=5)
clear_button.pack(side=LEFT, padx=5)

# Создаем кнопки для функций
add_function_buttons()

# Метка для отображения результата
result_label = Label(frame_result, text="Результат появится здесь")
result_label.pack()

# Компоновка
frame_input.pack(pady=10)
func_frame = Frame(root)
func_frame.pack(pady=5)
frame_result.pack(pady=10)

root.mainloop()