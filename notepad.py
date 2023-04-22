import tkinter as tk
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        text.delete(1.0, tk.END)
        with open(file, "r") as file_to_read:
            text.insert(tk.INSERT, file_to_read.read())
        update_word_count()

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "w") as file_to_write:
            file_to_write.write(text.get(1.0, tk.END))

def update_word_count(event=None):
    content = text.get(1.0, tk.END).strip()
    word_count = len(content.split())
    word_count_label.config(text=f"Word count: {word_count}")

root = tk.Tk()
root.title("Python Notepad")



text = tk.Text(root, wrap=tk.WORD, font=("Consolas", 14), bg='#1e1e1e', fg='#d4d4d4', insertbackground='white', selectbackground='#3c3c3c', undo=True)
text.pack(expand=True, fill=tk.BOTH)

text.bind("<KeyRelease>", update_word_count)
def update_word_count(event=None):
    content = text.get(1.0, tk.END).strip()
    word_count = len(content.split())
    word_count_label.config(text=f"Word count: {word_count}")

text.bind("<KeyRelease>", update_word_count)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

word_count_label = tk.Label(root, text="Word count: 0", bg='#1e1e1e', fg='#d4d4d4')
word_count_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=5, pady=5)

root.mainloop()
