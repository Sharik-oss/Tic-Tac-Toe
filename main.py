from tkinter import *
from tkinter import messagebox

window = Tk()
window.resizable(False, False)
window.title('Tic Tac Toe')
current_chr = "X"
play_area = Frame(window, width=400, height=500, bg='White')
window.geometry("350x400")
X_points = []
O_points = []
XO_points = []


def play_again():
    global current_chr
    current_chr = 'X'
    for point in XO_points:
        point.button.configure(state=NORMAL)
        point.reset()
    play_again_button.pack_forget()


play_again_button = Button(window, text="Play again", command=play_again)


def disable_game():
    for point in XO_points:
        point.button.configure(state=DISABLED)
    play_again_button.pack()

class XOPoints:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = Button(play_area, text="", width=10, height=5, command=self.set, bg='white')
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr
            if current_chr == "X":
                X_points.append(self)
                current_chr = "O"
            elif current_chr == "O":
                O_points.append(self)
                current_chr = "X"
        check_win()

    def reset(self):
        self.button.configure(text="", bg='white')
        if self.value == "X":
            X_points.remove(self)
        elif self.value == "O":
            O_points.remove(self)
        self.value = None


def play_again():
    for point in XO_points:
        point.button.configure(state=NORMAL)
        point.reset()


for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoints(x, y))


class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def check(self, for_char):
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False
        if for_char == 'X':
            for point in X_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        elif for_char == 'O':
            for point in O_points:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        return all([p1_satisfied, p2_satisfied, p3_satisfied])


winning_possibility = [
    WinningPossibility(1, 1, 1, 2, 1, 3),
    WinningPossibility(2, 1, 2, 2, 2, 3),
    WinningPossibility(3, 1, 3, 2, 3, 3),
    WinningPossibility(1, 1, 2, 1, 3, 1),
    WinningPossibility(1, 2, 2, 2, 3, 2),
    WinningPossibility(1, 3, 2, 3, 3, 3),
    WinningPossibility(1, 1, 2, 2, 3, 3),
    WinningPossibility(3, 1, 2, 2, 1, 3)
]


def check_win():
    for possibility in winning_possibility:
        if possibility.check('X'):
            messagebox.askokcancel('Info', 'Winner is X')
            disable_game()
        elif possibility.check('O'):
            messagebox.askokcancel('Info', "O is a winner!")
            disable_game()

    if len(X_points) + len(O_points) == 9:
        messagebox.askokcancel('Info', "It's a draw")
        disable_game()


play_area.pack(padx=10, pady=10)
window.mainloop()
