import tkinter as tk
from tkinter import font


class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}

# class for game
