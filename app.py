import tkinter as tk
import re

MIN_INTEGER = -2_147_483_648
MAX_INTEGER = 2_147_483_647
INPUT_ERROR = 'Ошибка: введите целые числа во все поля (от -2147483648 до 2147483647).'
POSITIVE_ERROR = 'Ошибка: длины сторон должны быть положительными числами.'
IMPOSSIBLE = 'Такой треугольник не существует.'
EQUILATERAL = 'Это равносторонний треугольник.'
ISOSCELES = 'Это равнобедренный треугольник.'
SCALENE = 'Это разносторонний треугольник.'


def check_triangle(a_text, b_text, c_text):
    sides = []
    for text in (a_text, b_text, c_text):
        text = text.strip()
        if len(text) > 100 or re.fullmatch(r'[+-]?[0-9]+', text) is None:
            return INPUT_ERROR
        number = int(text)
        if not MIN_INTEGER <= number <= MAX_INTEGER:
            return INPUT_ERROR
        sides.append(number)

    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return POSITIVE_ERROR
    if a + b <= c or a + c <= b or b + c <= a:
        return IMPOSSIBLE
    if a == b == c:
        return EQUILATERAL
    if a == b or a == c or b == c:
        return ISOSCELES
    return SCALENE


BACKGROUND = "#f8fafa"


def main():
    root = tk.Tk()
    root.title('Определение типа треугольника')
    root.geometry('550x335')
    root.resizable(False, False)
    root.configure(bg=BACKGROUND)
    root.option_add('*Font', ('Segoe UI', 10))

    tk.Label(
        root,
        text='Введите стороны треугольника',
        bg=BACKGROUND,
        fg='black',
    ).place(x=25, y=40, width=500, height=25)

    fields = []
    validate_length = root.register(lambda value: len(value) <= 100)
    for index in range(3):
        entry = tk.Entry(
            root,
            bg='white',
            fg='black',
            insertbackground='black',
            relief='solid',
            borderwidth=1,
            font=('Segoe UI', 10),
            validate='key',
            validatecommand=(validate_length, '%P'),
        )
        entry.place(x=12 + 183 * index, y=132, width=155, height=26)
        entry.insert(0, '1')
        fields.append(entry)

    tk.Label(
        root, text='Результат:', bg=BACKGROUND, fg='black', anchor='w'
    ).place(x=420, y=192, width=125, height=25)

    result = tk.StringVar(value='')
    tk.Label(
        root,
        textvariable=result,
        bg=BACKGROUND,
        fg='black',
        anchor='nw',
        justify='left',
        wraplength=174,
        font=('Segoe UI', 9),
    ).place(x=365, y=224, width=177, height=105)

    def calculate(event=None):
        result.set(check_triangle(*(field.get() for field in fields)))

    tk.Button(
        root,
        text='Посчитать',
        command=calculate,
        bg="#000000",
        fg="#ffffff",
        activebackground="#f5f5f5",
        activeforeground="#ffffff",
        relief='solid',
        borderwidth=1,
        cursor='hand2',
    ).place(x=195, y=221, width=155, height=41)

    root.bind('<Return>', calculate)
    root.bind('<KP_Enter>', calculate)
    fields[0].focus_set()
    fields[0].selection_range(0, tk.END)
    root.mainloop()


if __name__ == '__main__':
    main()
