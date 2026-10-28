import tkinter as tk 
from tkinter import messagebox


def check_winner():
    global winner

    for combo in [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]:
        if (
            button[combo[0]]["text"]
            == button[combo[1]]["text"]
            == button[combo[2]]["text"]
            != ""
        ):
            winner = True

            for i in combo:
                button[i].config(bg="green")

            messagebox.showinfo(
                "TIC-TAC-TOE",
                f"Player {button[combo[0]]['text']} wins!"
            )
            root.quit()
            return


def button_click(index):
    if button[index]["text"] == "" and not winner:
        button[index]["text"] = current_player
        check_winner()

        if winner:
            return

        if all(btn["text"] != "" for btn in button):
            messagebox.showinfo("TIC-TAC-TOE", "It's a draw!")
            root.quit()
            return

        toggle_player()


def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"player {current_player} s turn")

root = tk.Tk()
root.title("TIC-TAC-TOE")

button = [tk.Button(root, text="",font=("areal" ,25), width=6 , height=2 , command=lambda i=i: button_click(i)) for i in range( 9) ]

for i , btn in enumerate(button):
    btn.grid(row=i // 3 , column=i % 3)

current_player="X"
winner  = False
label =tk.Label(root , text=f"player {current_player}'s turn " , font=("areal" , 17))
label.grid(row=3 , column=0 , columnspan=3)

root.mainloop()

