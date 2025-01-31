import tkinter as tk
import random

root = tk.Tk()
photo = tk.PhotoImage(file='resourses/game_icon.png')
root.iconphoto(False, photo)
root.title("Randomin: Угадай число.")
root.config(bg='#bb9fcc')
root.geometry("500x600+400+100")
root.resizable(False, False)

font_large = ('Arial', 16)
font_medium = ('Arial', 14)

label_welcome = tk.Label(
    root, text="Welcome to the Randomin!", font=font_large)
label_welcome.grid(row=0, column=0, columnspan=2, pady=20, sticky='ew')

label_range = tk.Label(
    root, text="Enter the array of number: ", font=font_medium)
label_range.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_range = tk.Entry(root, font=font_medium, width=20)
entry_range.grid(row=1, column=1, padx=10, pady=5, sticky='w')

label_guess = tk.Label(root, text="Enter your choice: ", font=font_medium)
label_guess.grid(row=3, column=0, padx=10, pady=5, sticky='e')

entry_guess = tk.Entry(root, state='disabled', font=font_medium, width=20)
entry_guess.grid(row=3, column=1, padx=10, pady=5,
                 sticky='w')

label_result = tk.Label(root, text="", font=font_medium)

count_health = 3
secret_number = None


def update_result(message):
    label_result.grid(row=5, column=0, columnspan=2, pady=20)
    label_result.config(text=message)


def toggle_guess_button(show=True):
    if show:
        button_guess.grid(row=4, column=0, columnspan=2, pady=10)
    else:
        button_guess.grid_remove()


def toggle_guess_entry(enabled=True):
    if enabled:
        entry_guess.config(state='normal')
    else:
        entry_guess.config(state='disabled')


def generate_number():
    global count_health, secret_number
    try:
        max_value = int(entry_range.get())
        secret_number = random.randint(0, max_value)
        count_health = 3
        update_result(
            f"Number generated! Guess the number from 0 to {max_value}")
        toggle_guess_button(True)
        entry_guess.delete(0, 'end')
        entry_range.delete(0, 'end')
        toggle_guess_entry(True)

    except ValueError:
        label_result.config(text="Incorrect input! Enter the number.")


def check_guess():
    global count_health
    try:
        user_guess = int(entry_guess.get())
        if user_guess == secret_number:
            update_result("Congratulations! You guessed the number!")
            toggle_guess_button(False)
            toggle_guess_entry(False)
            entry_guess.delete(0, 'end')
        else:
            entry_guess.delete(0, 'end')
            count_health -= 1
            if count_health == 0:
                update_result(f"You lost! The number was {secret_number}")
                toggle_guess_button(False)
                toggle_guess_entry(False)
            else:
                if user_guess > secret_number:
                    update_result(
                        f"No, the number is lower! {count_health} attempts remaining.")
                else:
                    update_result(
                        f"No, the number is higher! {count_health} attempts remaining.")

    except ValueError:
        update_result("Enter the correct number!")


button_start = tk.Button(root, text="New game",
                         command=generate_number, font=font_medium)
button_start.grid(row=2, column=0, columnspan=2, pady=10)

button_guess = tk.Button(root, text="Let's try!",
                         command=check_guess, font=font_medium)
button_guess.grid(row=4, column=0, columnspan=2, pady=10)
toggle_guess_button(False)

root.mainloop()
