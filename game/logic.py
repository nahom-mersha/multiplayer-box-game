import random

class Player():
    def __init__(self, player_ids, canvas, keys_dict):
        self.player_ids = player_ids
        self.canvas = canvas
        self.keys_dict = keys_dict
    def move_player(self, player_id, speed, direction):
        match direction:
            case "left":
                self.canvas.move(player_id, -speed, 0)
            case "right":
                self.canvas.move(player_id, speed, 0)
            case "down":
                self.canvas.move(player_id, 0, speed)
            case "up":
                self.canvas.move(player_id, 0, -speed)
            case _:
                pass
    def update_movement(self): 
        if len(self.player_ids) > 0:
            if self.keys_dict["a"] == 1:
                self.move_player(self.player_ids[0], 10, "left")
            if self.keys_dict["d"] == 1:
                self.move_player(self.player_ids[0], 10, "right")
            if self.keys_dict["s"] == 1:
                self.move_player(self.player_ids[0], 10, "down")
            if self.keys_dict["w"] == 1:
                self.move_player(self.player_ids[0], 10, "up")
        if len(self.player_ids) > 1:
            if self.keys_dict["Left"] == 1:
                self.move_player(self.player_ids[1], 10, "left")
            if self.keys_dict["Right"] == 1:
                self.move_player(self.player_ids[1], 10, "right")
            if self.keys_dict["Down"] == 1:
                self.move_player(self.player_ids[1], 10, "down")
            if self.keys_dict["Up"] == 1:
                self.move_player(self.player_ids[1], 10, "up")
        if len(self.player_ids) > 2:
            if self.keys_dict["j"] == 1:
                self.move_player(self.player_ids[2], 10, "left")
            if self.keys_dict["l"] == 1:
                self.move_player(self.player_ids[2], 10, "right")
            if self.keys_dict["k"] == 1:
                self.move_player(self.player_ids[2], 10, "down")
            if self.keys_dict["i"] == 1:
                self.move_player(self.player_ids[2], 10, "up")
        if len(self.player_ids) > 3:
            if self.keys_dict["v"] == 1:
                self.move_player(self.player_ids[3], 10, "left")
            if self.keys_dict["n"] == 1:
                self.move_player(self.player_ids[3], 10, "right")
            if self.keys_dict["b"] == 1:
                self.move_player(self.player_ids[3], 10, "down")
            if self.keys_dict["g"] == 1:
                self.move_player(self.player_ids[3], 10, "up")
        self.canvas.after(10, self.update_movement)   
class KeyHandler():
    def __init__(self, root):
        self.keys_dict = {
            "a" : 0 , "d" : 0 , "s" : 0 , "w" : 0 , 
            "Left" : 0 , "Right" : 0 , "Up" : 0 , "Down" : 0 , 
            "j" : 0 , "l" : 0 , "i" : 0 , "k" : 0 , 
            "v" : 0 , "n" : 0 , "g" : 0 , "b" : 0
                    }
        self.root = root

    def update_key_press(self, event):
        key = event.keysym
        if key in self.keys_dict:
            self.keys_dict[key] = 1
    def update_key_release(self, event):
        key = event.keysym
        if key in self.keys_dict:
            self.keys_dict[key] = 0

    def binding_keys(self):
        self.root.bind("<KeyPress>", self.update_key_press)
        self.root.bind("<KeyRelease>", self.update_key_release)

class food():
    def __init__(self):
        self.size = 10
        self.food_id = None
    def draw(self, canvas):
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        random_x = random.uniform(0, width - self.size)
        random_y = random.uniform(0, height - self.size)
        self.food_id = canvas.create_rectangle(random_x, random_y, random_x + self.size, random_y + self.size)
    