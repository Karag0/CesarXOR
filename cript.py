import tkinter as tk
from tkinter import messagebox
def show_about():
    messagebox.showinfo("О программе", texts[language]['about_message'])
    
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if 'A' <= char <= 'Z':
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'А' <= char <= 'Я':
            encrypted += chr((ord(char) - ord('А') + shift) % 32 + ord('А'))
        elif 'а' <= char <= 'я':
            encrypted += chr((ord(char) - ord('а') + shift) % 32 + ord('а'))
        else:
            encrypted += char
    return encrypted

def permute(text):
    return text[::-1]

def xor_encrypt(text, key):
    return ''.join(chr(ord(c) ^ key) for c in text)

def encrypt(text, shift, key):
    caesar_encrypted = caesar_encrypt(text, shift)
    permuted = permute(caesar_encrypted)
    final_encrypted = xor_encrypt(permuted, key)
    return final_encrypted

def decrypt(text, shift, key):
    xor_decrypted = xor_encrypt(text, key)
    permuted_back = permute(xor_decrypted)
    final_decrypted = caesar_encrypt(permuted_back, -shift)
    return final_decrypted

def on_encrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    key = int(key_entry.get())
    encrypted_text = encrypt(text, shift, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def on_decrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    key = int(key_entry.get())
    decrypted_text = decrypt(text, shift, key)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

def copy_to_clipboard():
    text = output_text.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(text)

def paste_from_clipboard():
    try:
        text = root.clipboard_get()
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, text)
    except tk.TclError:
        tk.messagebox.showwarning("Вставка", "Буфер обмена пуст!")

def clear_output():
    # Функция для очистки текстового поля вывода
    output_text.delete("1.0", tk.END)

# Создание основного окна
root = tk.Tk()
root.title("Мега Сложный Шифратор")

# Ввод текста
input_label = tk.Label(root, text="Введите текст:")
input_label.pack()
input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# Сдвиг
shift_label = tk.Label(root, text="Введите сдвиг:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Ключ для XOR
key_label = tk.Label(root, text="Введите ключ для XOR:")
key_label.pack()
key_entry = tk.Entry(root)
key_entry.pack()

# Кнопки
encrypt_button = tk.Button(root, text="Зашифровать", command=on_encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Дешифровать", command=on_decrypt)
decrypt_button.pack()

copy_button = tk.Button(root, text="Скопировать в буфер", command=copy_to_clipboard)
copy_button.pack()

paste_button = tk.Button(root, text="Вставить из буфера", command=paste_from_clipboard)
paste_button.pack()

# Кнопка для очистки вывода
clear_button = tk.Button(root, text="Очистить вывод", command=clear_output)
clear_button.pack()

# Вывод результата
output_label = tk.Label(root, text="Результат:")
output_label.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# Функции для смены языка
def change_language():
    global language
    language = 'en' if language == 'ru' else 'ru'
    update_text()

def update_text():
    input_label.config(text=texts[language]['input_label'])
    shift_label.config(text=texts[language]['shift_label'])
    key_label.config(text=texts[language]['key_label'])
    encrypt_button.config(text=texts[language]['encrypt_button'])
    decrypt_button.config(text=texts[language]['decrypt_button'])
    copy_button.config(text=texts[language]['copy_button'])
    paste_button.config(text=texts[language]['paste_button'])
    clear_button.config(text=texts[language]['clear_button'])
    about_button.config(text=texts[language]['about_button'])
    output_label.config(text=texts[language]['output_label'])


# Переменная для хранения текущего языка
language = 'ru'

# Словарь с текстами на русском и английском
texts = {
    'ru': {
        'input_label': "Введите текст:",
        'shift_label': "Введите сдвиг:",
        'key_label': "Введите ключ для XOR:",
        'encrypt_button': "Зашифровать",
        'decrypt_button': "Дешифровать",
        'copy_button': "Скопировать в буфер",
        'paste_button': "Вставить из буфера",
        'clear_button': "Очистить вывод",
        'about_button': "О программе",
        'output_label': "Результат:",
        'about_message': "Программа разработана Владиславом Ореховым для школьного проекта.\n Исходный код https://github.com/Karag0/CesarXOR"
    },
    'en': {
        'input_label': "Enter text:",
        'shift_label': "Enter shift:",
        'key_label': "Enter XOR key:",
        'encrypt_button': "Encrypt",
        'decrypt_button': "Decrypt",
        'copy_button': "Copy to clipboard",
        'paste_button': "Paste from clipboard",
        'clear_button': "Clear output",
        'about_button': "About",
        'output_label': "Result:",
        'about_message': "The program was developed by Vladislav Orekhov for a school project.\nSource code: https://github.com/Karag0/CesarXOR"
    }
}


# Кнопка "О программе"
about_button = tk.Button(root, text=texts[language]['about_button'], command=show_about)
about_button.pack()

# Добавьте кнопку для смены языка
language_button = tk.Button(root, text="Change language", command=change_language)
language_button.pack()

# Обновите текст интерфейса в начале
update_text()

# Запуск основного цикла
root.mainloop()
