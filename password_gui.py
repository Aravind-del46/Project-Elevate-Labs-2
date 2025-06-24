import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn

# --- Wordlist logic ---
def leetspeak(word):
    return word.replace('a', '@').replace('e', '3').replace('o', '0').replace('i', '1').replace('s', '$')

def generate_wordlist(info):
    variants = set()
    for item in info:
        item = item.lower()
        variants.update([item, leetspeak(item), item[::-1]])
        for year in ['2023', '2024', '007']:
            variants.add(item + year)
            variants.add(year + item)
    return variants

def save_wordlist_to_file(words):
    with open("custom_wordlist.txt", "w") as file:
        for word in words:
            file.write(word + "\n")

# --- Password strength logic ---
def check_password_strength():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Input Missing", "Please enter a password.")
        return

    result = zxcvbn(password)
    score = result['score']
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']
    suggestions = result['feedback']['suggestions']

    output = f"Score (0-4): {score}\nCrack Time: {crack_time}"
    if suggestions:
        output += f"\nSuggestions: {', '.join(suggestions)}"
    label_result.config(text=output)

# --- GUI for wordlist ---
def generate_wordlist_gui():
    name = entry_name.get()
    dob = entry_dob.get()
    pet = entry_pet.get()

    if not (name and dob and pet):
        messagebox.showwarning("Input Missing", "Please fill in all fields.")
        return

    words = generate_wordlist([name, dob, pet])
    save_wordlist_to_file(words)
    label_wordlist_result.config(text="✅ Wordlist saved as custom_wordlist.txt")

# --- GUI setup ---
root = tk.Tk()
root.title("🔐 Password Strength Analyzer & Wordlist Generator")
root.geometry("500x400")
root.resizable(False, False)

# --- Password strength UI ---
frame_pwd = tk.LabelFrame(root, text="Password Strength Checker", padx=10, pady=10)
frame_pwd.pack(padx=10, pady=10, fill="x")

tk.Label(frame_pwd, text="Enter Password:").grid(row=0, column=0, sticky="w")
entry_password = tk.Entry(frame_pwd, width=40, show="*")
entry_password.grid(row=0, column=1)

btn_check = tk.Button(frame_pwd, text="Check Strength", command=check_password_strength)
btn_check.grid(row=1, column=0, columnspan=2, pady=5)

label_result = tk.Label(frame_pwd, text="", fg="blue", justify="left")
label_result.grid(row=2, column=0, columnspan=2, sticky="w")

# --- Wordlist generator UI ---
frame_gen = tk.LabelFrame(root, text="Custom Wordlist Generator", padx=10, pady=10)
frame_gen.pack(padx=10, pady=10, fill="x")

tk.Label(frame_gen, text="Name:").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_gen, width=30)
entry_name.grid(row=0, column=1)

tk.Label(frame_gen, text="DOB (YYYYMMDD):").grid(row=1, column=0, sticky="w")
entry_dob = tk.Entry(frame_gen, width=30)
entry_dob.grid(row=1, column=1)

tk.Label(frame_gen, text="Pet Name:").grid(row=2, column=0, sticky="w")
entry_pet = tk.Entry(frame_gen, width=30)
entry_pet.grid(row=2, column=1)

btn_generate = tk.Button(frame_gen, text="Generate Wordlist", command=generate_wordlist_gui)
btn_generate.grid(row=3, column=0, columnspan=2, pady=5)

label_wordlist_result = tk.Label(frame_gen, text="", fg="green")
label_wordlist_result.grid(row=4, column=0, columnspan=2, sticky="w")

root.mainloop()
