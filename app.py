import random
import tkinter as tk
from tkinter import messagebox

def generate_passwords():
    full_name = name_entry.get().strip().lower().replace(" ", "")
    birth_date = birth_entry.get().strip().replace(".", "").replace("-", "")
    
    if not full_name or not birth_date:
        messagebox.showerror("Ошибка", "Введите ФИО и дату рождения!")
        return

    special_chars = ["@", "!", "*", "_", "#"]
    passwords = []

    for _ in range(10):
        part1 = random.choice([full_name[:3], full_name[-3:], full_name[:5], full_name[-5:]])
        part2 = random.choice([birth_date[:4], birth_date[-4:], birth_date])
        part3 = random.choice(special_chars) + str(random.randint(10, 99))
        
        password = part1 + part2 + part3
        passwords.append(password)

    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "\n".join(passwords))
    result_text.config(state="disabled")

# --- Интерфейс Tkinter ---
root = tk.Tk()
root.title("Генератор паролей")

tk.Label(root, text="Введите ФИО:").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Введите дату рождения (дд.мм.гггг):").pack()
birth_entry = tk.Entry(root, width=20)
birth_entry.pack()

generate_button = tk.Button(root, text="Сгенерировать пароли", command=generate_passwords)
generate_button.pack()

result_text = tk.Text(root, height=10, width=40, state="disabled")
result_text.pack()

root.mainloop()
