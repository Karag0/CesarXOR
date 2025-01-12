import tkinter as tk
from tkinter import messagebox

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
    output_text.delete("1.0", tk.END)

def show_about():
    messagebox.showinfo("О программе", "Программа разработана Владиславом Ореховым для школьного проекта.\nОна не обеспечивает должный уровень безопасности.")

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

# Кнопка "О программе"
about_button = tk.Button(root, text="О программе", command=show_about)
about_button.pack()

# Вывод результата
output_label = tk.Label(root, text="Результат:")
output_label.pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

# Запуск основного цикла
root.mainloop()
