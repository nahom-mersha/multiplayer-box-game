import tkinter as tk
#import visuals.render as render
from visuals import render

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multiplayer Game")
        self.root.state("zoomed")
        self.root.config(bg="black")
        self.canvas = tk.Canvas(self.root, bg="grey")
        self.canvas.pack(padx=10, pady=10, fill="both", expand=True) 
        renderer = render.Renderer(self.canvas)
        self.root.update()
        self.player_ids = []
        self.player_ids.extend(renderer.create_players(4))
        print(self.player_ids)
    def run(self):
       self.root.mainloop()



