import utils.geometry as geometry
class Renderer():
    def __init__(self, canvas):
        self.canvas = canvas
        self.pheight = 30
        self.pwidth = 30
        self.color_list = ["blue", "red", "green", "yellow"]
        
    def create_players(self, player_count):
        canvas_coordinats = geometry.get_canvas_height_width(self.canvas)
        bbox = (0, 0, canvas_coordinats[0], canvas_coordinats[1])
        coordinats = geometry.get_four_quadrant_centers(bbox)
        print(coordinats)
        count = 0
        for position in coordinats:
            if count > player_count:
                break
            self.canvas.create_rectangle(position[0]-self.pwidth/2, position[1]-self.pheight/2, position[0]+self.pwidth/2, position[1]+self.pheight/2, fill=self.color_list[count])
            count += 1
