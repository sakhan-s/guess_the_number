import random
import sys
import tkinter as tk
from tkinter import filedialog

sys.stdout.reconfigure(encoding='utf-8')


# Задаем диапазон чисел, которые может загадать компьютер
MIN_NUMBER = 1
MAX_NUMBER = 100

# Генерируем случайное число, которое нужно угадать
number = random.randint(MIN_NUMBER, MAX_NUMBER)

# Настройки игры
attempts = 0  # количество попыток
max_attempts = 10  # максимальное количество попыток

# Создаем главное окно
root = tk.Tk()
root.title('Игра "Угадай число"')

# Устанавливаем размер окна и расположение по центру экрана
window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Создаем холст для отображения фоновой картинки
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Создаем текстовое поле для вывода сообщений и добавляем автоматический скроллинг
message_field = tk.Text(canvas, height=30, width=40, font=("Arial", 14))
message_field.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(message_field)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
message_field.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=message_field.yview)

# Создаем текстовое поле для ввода числа
guess_field = tk.Entry(canvas, font=("Arial", 14))
guess_field.pack()

# Создаем текстовое поле для отображения предыдущих попыток
previous_guess_field = tk.Text(canvas, height=5, width=40, font=("Arial", 14), state='disabled')
previous_guess_field.pack()

# Создаем кнопку для отправки ответа
submit_button = tk.Button(canvas, text='Угадать!', font=("Arial", 14))

# Создаем кнопку для сброса игры
reset_button = tk.Button(canvas, text='Сбросить', font=("Arial", 14), state='disabled')

# Обработчик события нажатия на кнопку
def on_submit_click():
    global attempts

    # Получаем ответ игрока
    guess = int(guess_field.get())

    # Отображаем предыдущий ввод
    previous_guess_field.config(state='normal')
    previous_guess_field.insert(tk.END, f'{guess}\n')
    previous_guess_field.config(state='disabled')

    # Проверяем, угадал ли игрок число
    if guess < number:
        message_field.insert(tk.END, 'Загаданное число больше\n')
    elif guess > number:
        message_field.insert(tk.END, 'Загаданное число меньше\n')
    else:
        message_field.insert(tk.END, f'Вы угадали число {number} за {attempts} попыток!\n')
        submit_button.config(state=tk.DISABLED)  # Отключаем кнопку
        guess_field.config(state=tk.DISABLED)  # Отключаем поле ввода
        reset_button.config(state=tk.NORMAL)  # Включаем кнопку сброса игры
        return

    # Обновляем счетчик попыток
    attempts += 1

    # Проверяемпродолжение кода:

    # исчерпал ли игрок лимит попыток
    if attempts >= max_attempts:
        message_field.insert(tk.END, f'Вы проиграли. Было загадано число {number}\n')
        submit_button.config(state=tk.DISABLED)  # Отключаем кнопку
        guess_field.config(state=tk.DISABLED)  # Отключаем поле ввода
        reset_button.config(state=tk.NORMAL)  # Включаем кнопку сброса игры
        return

    # Очищаем поле ввода
    guess_field.delete(0, tk.END)
    # Ставим фокус на поле ввода
    guess_field.focus()
    # Ставим фокус на последнее сообщение
    message_field.see(tk.END)

# Назначаем обработчик события нажатия на кнопку
submit_button.config(command=on_submit_click)
submit_button.pack()

# Обработчик события нажатия на кнопку сброса игры
def on_reset_click():
    global number, attempts
    # Генерируем новое число
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    # Сбрасываем счетчик попыток
    attempts = 0
    # Очищаем поля ввода и вывода
    guess_field.delete(0, tk.END)
    message_field.delete(1.0, tk.END)
    previous_guess_field.config(state='normal')
    previous_guess_field.delete(1.0, tk.END)
    previous_guess_field.config(state='disabled')
    # Включаем кнопку угадывания числа и поле ввода
    submit_button.config(state=tk.NORMAL)
    guess_field.config(state=tk.NORMAL)
    # Отключаем кнопку сброса игры
    reset_button.config(state=tk.DISABLED)

# Назначаем обработчик события нажатия на кнопку сброса игры
reset_button.config(command=on_reset_click)
reset_button.pack()

# Запускаем главный цикл обработки событий
root.mainloop()